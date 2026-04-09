<?php
header('Content-Type: application/json');

// Receives user input from HTML
$input = json_decode(file_get_contents('php://input'), true);
$message = $input['message'];

// Forwards it to the Python Flask server
$ch = curl_init('http://127.0.0.1:5000/chat');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode(['message' => $message]));
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>