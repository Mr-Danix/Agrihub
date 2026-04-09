from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import stripe
import json
import os
import time

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app) # Allows your HTML to talk to this Python script

# Set OpenAI API key (make sure to set OPENAI_API_KEY environment variable)
openai.api_key = os.getenv('OPENAI_API_KEY')
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

ORDERS_FILE = 'orders.json'
SHIPPING_FEE = 250


def load_orders():
    if os.path.exists(ORDERS_FILE):
        try:
            with open(ORDERS_FILE, 'r', encoding='utf-8') as fh:
                return json.load(fh)
        except Exception:
            return []
    return []


def save_orders(orders):
    with open(ORDERS_FILE, 'w', encoding='utf-8') as fh:
        json.dump(orders, fh, indent=2, ensure_ascii=False)


@app.route('/')
def root():
    return app.send_static_file('home.html')

# Knowledge Base from https://mr-danix.github.io/Agrihub/
AGRI_DATA = {
    "hi": "Hey, I'm Agrihub's Chatbot/Assistant.I'm here to answer Your Question about this website.",
    "about": "AgriHub is an Ethiopian digital exchange connecting farmers and buyers directly. Ethiopia's Digital Harvest - Connect directly with local farmers. Get the best prices, support local communities, and eat fresh. For farmers: Connect directly with local Buyers.",
    "products": "We offer a wide variety of Ethiopian products including Teff, Red Onions, Organic Coffee, Fresh Garlic, Sidama Coffee, Green Chili, Barley, Ginger Root, Bananas, Avocado, Potatoes, Tomatoes, Black Cumin, Wheat, Papaya, Cabbage, Carrots, Lemons, Chickpeas, Lentils, Peanuts, Mangoes, Maize, Butter (Qibe), Sweet Potato, Sorghum, Strawberries, Green Beans, Linseed, Oranges, Buna (Raw Beans), Hops (Gesho), Red Chili (Berbere), Pineapple, Guava, Faba Beans, Pumpkin, Sesame Seeds, Grapes, Beetroot, Millet, Custard Apple, Leeks, Sunflower Seeds, Eggplant, Oats, Key Sir, Black Pepper, and Apple. Prices range from 12 to 200 ETB per kg depending on the product.",
    "signup": "You can register as a Farmer to sell or a Buyer to shop on our Sign Up page.",
    
    "mission": "Our mission is to eliminate middlemen and ensure fair prices for Ethiopian farmers.",
    "tutorial": "Before we start our business lets take a tutorial to get familiar with our platform.",
    "shopping": "Start shopping by visiting our products page. Add items to your cart and proceed to checkout.",
    "selling": "Farmers can start selling by visiting the sell page and listing their products.",
    "contact": "Contact us for support. Our team will fix your problems as fast as possible.",
    "cart": "Your cart shows the items you've added. You can remove items or proceed to checkout.",
    "delivery": "After checkout, provide delivery details to get your fresh products.",
    "default": "I'm not sure about that, Ask me questions related to this website!"
}

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get("message", "")
    
    if not openai.api_key:
        # Fallback to keyword matching if no API key
        user_lower = user_msg.lower()
        if "hi" in user_input:
            return AGRI_DATA["hi"]
        if any(word in user_lower for word in ["product", "coffee", "teff", "vegetable", "fruit", "grain", "buy", "shop", "market"]):
            reply = AGRI_DATA["products"]
        elif any(word in user_lower for word in ["who", "what", "about", "agrihub", "company", "platform", "ethiopia", "harvest"]):
            reply = AGRI_DATA["about"]
        elif any(word in user_lower for word in ["join", "sign up", "account", "register", "farmer", "buyer"]):
            reply = AGRI_DATA["signup"]
        elif any(word in user_lower for word in ["mission", "goal", "purpose", "why"]):
            reply = AGRI_DATA["mission"]
        elif any(word in user_lower for word in ["tutorial", "start", "begin", "learn"]):
            reply = AGRI_DATA["tutorial"]
        elif any(word in user_lower for word in ["shopping", "purchase", "order"]):
            reply = AGRI_DATA["shopping"]
        elif any(word in user_lower for word in ["selling", "sell", "list"]):
            reply = AGRI_DATA["selling"]
        elif any(word in user_lower for word in ["contact", "help", "support", "problem"]):
            reply = AGRI_DATA["contact"]
        elif any(word in user_lower for word in ["cart", "basket"]):
            reply = AGRI_DATA["cart"]
        elif any(word in user_lower for word in ["delivery", "shipping", "checkout"]):
            reply = AGRI_DATA["delivery"]
        else:
            reply = AGRI_DATA["default"]
    else:
        # Use OpenAI to generate response based on AgriHub knowledge
        context = "\n".join([f"{key}: {value}" for key, value in AGRI_DATA.items()])
        prompt = f"You are a helpful chatbot for AgriHub, an Ethiopian digital farming platform. Answer questions based on the following information:\n{context}\n\nUser: {user_msg}\nAssistant:"
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant for AgriHub, providing information about the platform, products, and services based on the given knowledge base."},
                    {"role": "user", "content": user_msg}
                ],
                max_tokens=150,
                temperature=0.7
            )
            reply = response.choices[0].message.content.strip()
        except Exception as e:
            reply = f"Sorry, I encountered an error: {str(e)}. Falling back to basic responses."
            # Fallback logic here if needed

    return jsonify({"reply": reply})

@app.route('/create-order', methods=['POST'])
def create_order():
    data = request.get_json() or {}
    required_fields = ['name', 'phone', 'region', 'address', 'paymentMethod', 'items']
    if any(not data.get(field) for field in required_fields):
        return jsonify({'error': 'Missing required order data.'}), 400

    payment_method = data.get('paymentMethod')
    payment_reference = (data.get('paymentReference') or '').strip()
    if payment_method not in ['Cash on Delivery', 'Card Payment'] and len(payment_reference) < 3:
        return jsonify({'error': 'Payment reference is required for Telebirr or CBE Birr.'}), 400

    items = data.get('items', [])
    total_price = sum(float(item.get('price', 0)) for item in items)
    order_total = total_price + SHIPPING_FEE
    order_id = str(int(time.time() * 1000))

    order = {
        'orderId': order_id,
        'name': data['name'],
        'phone': data['phone'],
        'region': data['region'],
        'address': data['address'],
        'paymentMethod': payment_method,
        'paymentReference': payment_method == 'Cash on Delivery' and 'cash' or payment_reference,
        'items': items,
        'orderTotal': order_total,
        'shippingFee': SHIPPING_FEE,
        'status': 'pending',
        'createdAt': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
    }

    orders = load_orders()
    orders.append(order)
    save_orders(orders)

    return jsonify({'success': True, 'message': 'Order recorded. We will verify payment and prepare delivery.'})


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    if not stripe.api_key:
        return jsonify({'error': 'Stripe secret key is not configured on the server.'}), 500

    data = request.get_json() or {}
    required_fields = ['name', 'phone', 'region', 'address', 'paymentMethod', 'items']
    if any(not data.get(field) for field in required_fields):
        return jsonify({'error': 'Missing required order data.'}), 400

    items = data.get('items', [])
    if len(items) == 0:
        return jsonify({'error': 'Your cart is empty.'}), 400

    total_price = sum(float(item.get('price', 0)) for item in items)
    order_total = total_price + SHIPPING_FEE
    order_id = str(int(time.time() * 1000))

    grouped = {}
    for item in items:
        key = f"{item.get('name')}|{item.get('price')}"
        grouped.setdefault(key, {'name': item.get('name'), 'price': float(item.get('price', 0)), 'quantity': 0})
        grouped[key]['quantity'] += 1

    line_items = []
    for grouped_item in grouped.values():
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': grouped_item['name']},
                'unit_amount': int(round(grouped_item['price'] * 100))
            },
            'quantity': grouped_item['quantity']
        })

    line_items.append({
        'price_data': {
            'currency': 'usd',
            'product_data': {'name': 'Agrihub Shipping Fee'},
            'unit_amount': int(round(SHIPPING_FEE * 100))
        },
        'quantity': 1
    })

    order = {
        'orderId': order_id,
        'name': data['name'],
        'phone': data['phone'],
        'region': data['region'],
        'address': data['address'],
        'paymentMethod': 'Card Payment',
        'items': items,
        'orderTotal': order_total,
        'shippingFee': SHIPPING_FEE,
        'status': 'pending_payment',
        'createdAt': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
        'stripeSessionId': None,
    }

    orders = load_orders()
    orders.append(order)
    save_orders(orders)

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=request.host_url + 'payment-success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.host_url + 'delivery.html',
            metadata={
                'order_id': order_id,
                'customer_name': data['name'],
                'phone': data['phone'],
                'region': data['region'],
                'address': data['address'],
            }
        )
        order['stripeSessionId'] = session.id
        save_orders(orders)
        return jsonify({'success': True, 'url': session.url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/payment-success')
def payment_success():
    session_id = request.args.get('session_id')
    if not session_id:
        return '<h1>Missing Stripe session ID.</h1>', 400

    if not stripe.api_key:
        return '<h1>Stripe is not configured on the server.</h1>', 500

    try:
        session = stripe.checkout.Session.retrieve(session_id)
    except Exception as e:
        return f'<h1>Unable to verify payment: {str(e)}</h1>', 500

    orders = load_orders()
    for order in orders:
        if order.get('stripeSessionId') == session_id:
            order['status'] = 'paid'
            save_orders(orders)
            break

    return f"""<html><head><script>window.location.href = '/order-success.html';</script></head><body></body></html>"""


if __name__ == '__main__':
    app.run(port=5000, debug=True)