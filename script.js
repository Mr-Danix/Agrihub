
const inventory = [
    { id: 1, name: "Premium Teff", price: 65, origin: "Amhara", icon: "🌾" },
    { id: 2, name: "Red Onions", price: 28, origin: "Oromia", icon: "🧅" },
    { id: 3, name: "Organic Coffee", price: 180, origin: "Jimma", icon: "☕" },
    { id: 4, name: "Fresh Garlic", price: 45, origin: "Tigray", icon: "🧄" },
    { id: 5, name: "Sidama Coffee", price: 180, origin: "Sidama", icon: "☕", cat: "Grains" },
    { id: 6, name: "Green Chili", price: 15, origin: "Butajira", icon: "🌶️", cat: "Vegetables" },
    { id: 7, name: "Barley", price: 40, origin: "Arsi", icon: "🌾", cat: "Grains" },
    { id: 8, name: "Ginger Root", price: 90, origin: "Wolaita", icon: "🫚", cat: "Vegetables" },
    { id: 9, name: "Bananas", price: 12, origin: "Arba Minch", icon: "🍌", cat: "Fruits" },
    { id: 10, name: "Avocado", price: 35, origin: "Wondo Genet", icon: "🥑", cat: "Fruits" },
    { id: 11, name: "Potatoes", price: 22, origin: "Shashemene", icon: "🥔", cat: "Vegetables" },
    { id: 12, name: "Tomatoes", price: 18, origin: "Meki", icon: "🍅", cat: "Vegetables" },
    { id: 13, name: "Black Cumin", price: 110, origin: "Bale", icon: "🧂", cat: "Specialty" },
    { id: 14, name: "Wheat", price: 55, origin: "Hoseana", icon: "🌾", cat: "Grains" },
    { id: 15, name: "Papaya", price: 30, origin: "Awash", icon: "🥭", cat: "Fruits" },
    { id: 16, name: "Cabbage", price: 14, origin: "Holeta", icon: "🥬", cat: "Vegetables" },
    { id: 17, name: "Carrots", price: 20, origin: "Kombolcha", icon: "🥕", cat: "Vegetables" },
    { id: 18, name: "Lemons", price: 25, origin: "Dire Dawa", icon: "🍋", cat: "Fruits" },
    { id: 19, name: "Chickpeas", price: 60, origin: "Gonder", icon: "🫘", cat: "Grains" },
    { id: 20, name: "Lentils", price: 85, origin: "Debre Birhan", icon: "🥘", cat: "Grains" },
    { id: 21, name: "Peanuts", price: 95, origin: "Gambela", icon: "🥜", cat: "Specialty" },
    { id: 22, name: "Mangoes", price: 40, origin: "Assosa", icon: "🥭", cat: "Fruits" },
    { id: 23, name: "Maize", price: 32, origin: "Jimma", icon: "🌽", cat: "Grains" },
    { id: 24, name: "Butter (Qibe)", price: 450, origin: "Sheno", icon: "🧈", cat: "Specialty" },
    { id: 25, name: "Sweet Potato", price: 15, origin: "Wolaita", icon: "🍠", cat: "Vegetables" },
    { id: 26, name: "Sorghum", price: 38, origin: "Harar", icon: "🌾", cat: "Grains" },
    { id: 27, name: "Strawberries", price: 120, origin: "Debre Zeit", icon: "🍓", cat: "Fruits" },
    { id: 28, name: "Green Beans", price: 24, origin: "Ziway", icon: "🫛", cat: "Vegetables" },
    { id: 29, name: "Linseed", price: 75, origin: "Fiche", icon: "🌻", cat: "Specialty" },
    { id: 30, name: "Oranges", price: 45, origin: "Upper Awash", icon: "🍊", cat: "Fruits" },
    { id: 31, name: "Buna (Raw Beans)", price: 160, origin: "Yirgacheffe", icon: "🫘", cat: "Grains" },
    { id: 32, name: "Hops (Gesho)", price: 55, origin: "Enseno", icon: "🌿", cat: "Specialty" },
    { id: 33, name: "Red Chili (Berbere)", price: 130, origin: "Mareko", icon: "🌶️", cat: "Specialty" },
    { id: 34, name: "Pineapple", price: 65, origin: "Gojeb", icon: "🍍", cat: "Fruits" },
    { id: 35, name: "Guava", price: 22, origin: "Keffa", icon: "🍏", cat: "Fruits" },
    { id: 36, name: "Faba Beans", price: 48, origin: "Shoa", icon: "🫘", cat: "Grains" },
    { id: 37, name: "Pumpkin", price: 40, origin: "Gurage", icon: "🎃", cat: "Vegetables" },
    { id: 38, name: "Sesame Seeds", price: 90, origin: "Humera", icon: "🥣", cat: "Specialty" },
    { id: 39, name: "Grapes", price: 150, origin: "Zeway", icon: "🍇", cat: "Fruits" },
    { id: 40, name: "Beetroot", price: 26, origin: "Addis Alem", icon: "🧶", cat: "Vegetables" },
    { id: 41, name: "Millet", price: 42, origin: "Metekel", icon: "🌾", cat: "Grains" },
    { id: 42, name: "Custard Apple", price: 50, origin: "Dire Dawa", icon: "🍈", cat: "Fruits" },
    { id: 43, name: "Leeks", price: 18, origin: "Sendafa", icon: "🥬", cat: "Vegetables" },
    { id: 44, name: "Sunflower Seeds", price: 80, origin: "Afar", icon: "🌻", cat: "Specialty" },
    { id: 45, name: "Eggplant", price: 32, origin: "Meki", icon: "🍆", cat: "Vegetables" },
    { id: 46, name: "Oats", price: 50, origin: "Bale", icon: "🥣", cat: "Grains" },
    { id: 47, name: "Key Sir", price: 20, origin: "Akaki", icon: "🥗", cat: "Vegetables" },
    { id: 48, name: "Black Pepper", price: 200, origin: "Tepi", icon: "🫘", cat: "Specialty" },
    { id: 49, name: "Apple", price: 140, origin: "Chencha", icon: "🍎", cat: "Fruits" },
    { id: 50, name: "Fenugreek (Abish)", price: 70, origin: "Wollo", icon: "🌿", cat: "Specialty" }
];


function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const target = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', target);
    localStorage.setItem('agriTheme', target);
}


function addToCart(id) {
    let cart = JSON.parse(localStorage.getItem('agriCart')) || [];
    const item = inventory.find(p => p.id === id);
    cart.push(item);
    localStorage.setItem('agriCart', JSON.stringify(cart));
    updateCartUI();
    alert(`${item.name} added to cart!`);
}

function updateCartUI() {
    const cart = JSON.parse(localStorage.getItem('agriCart')) || [];
    const countEl = document.getElementById('cartCount');
    if (countEl) countEl.innerText = cart.length;

    const cartList = document.getElementById('cartItems');
    if (cartList) {
        if (cart.length === 0) {
            cartList.innerHTML = "<p class='muted'>Your cart is empty.</p>";
            document.getElementById('cartTotal').innerText = "0 ETB";
            return;
        }
        let total = 0;
        cartList.innerHTML = cart.map((item, idx) => {
            total += item.price;
            return `<div class="cart-row">
                <span>${item.icon} ${item.name}</span>
                <strong>${item.price} ETB</strong>
                <button onclick="removeItem(${idx})" class="del-btn">✕</button>
            </div>`;
        }).join('');
        document.getElementById('cartTotal').innerText = `${total} ETB`;
    }
}

function removeItem(index) {
    let cart = JSON.parse(localStorage.getItem('agriCart')) || [];
    cart.splice(index, 1);
    localStorage.setItem('agriCart', JSON.stringify(cart));
    updateCartUI();
}


function sendContact(e) {
    e.preventDefault();
    const status = document.getElementById('statusMsg');
    status.innerHTML = "Sending...";
    setTimeout(() => {
        status.innerHTML = "✅ Message Sent! Our team will contact you and fix your problem as much and fast as possible.";
        e.target.reset();
    }, 1500);
}


document.addEventListener('DOMContentLoaded', () => {
    const theme = localStorage.getItem('agriTheme') || 'light';
    document.documentElement.setAttribute('data-theme', theme);
    updateCartUI();
    
    const prodGrid = document.getElementById('prodGrid');
    if (prodGrid) {
        prodGrid.innerHTML = inventory.map(p => `
            <div class="panel fade-in">
                <div style="font-size:2.5rem">${p.icon}</div>
                <h3>${p.name}</h3>
                <p class="muted">${p.origin} Region</p>
                <div style="margin:10px 0; font-weight:bold">${p.price} ETB / kg</div>
                <button class="btn-main" onclick="addToCart(${p.id})">Add to Cart</button>
            </div>
        `).join('');
    }
});