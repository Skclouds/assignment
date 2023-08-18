# Restaurant Chat and Order APIs

This project demonstrates the implementation of two APIs using Flask and OpenAI's GPT-3.5 API. The APIs allow users to interact with a restaurant's chatbot for inquiries and place orders for items with their respective prices.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/restaurant-apis.git
   cd restaurant-apis
Install the required packages:
  pip install -r requirements.txt
2.Set your OpenAI API key:
Open python restaurant_api.py and replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key.
3.Run the application:
python restaurant_api.key
# API Endpoints
Chat API
Endpoint: /chat
Method: POST
Request Body:
{
  "question": "What is your restaurant's specialty?"
}
{
  "result": "Our restaurant is known for its exquisite seafood dishes and cozy ambiance."
}
# Order API
Endpoint: /order
Method: POST
Request Body:

{
  "item_name": "Grilled Salmon"
}
{
  "result": "Order for item: Grilled Salmon, price: 50 placed successfully."
}
# Usage
Use the /chat API to interact with the restaurant's chatbot by sending a question in the request body. You'll receive an auto-generated response from the chatbot.

Use the /order API to place an order for a menu item. Provide the item_name in the request body, and the API will return an order confirmation with the item's price.
# Disclaimer
This is a basic example for demonstration purposes. Ensure to handle security, error handling, and rate limiting before deploying to a production environment.
