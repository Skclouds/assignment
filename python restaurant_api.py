from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = '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'

# Restaurant data prompt for ChatGPT
restaurant_data_prompt = "Our restaurant offers a diverse menu with a variety of dishes at affordable prices. From mouthwatering appetizers to delectable desserts, we have something for everyone. Our location is in the heart of the city, making it convenient for you to dine with us. Ask me anything!"

# Chat API
@app.route('/chat', methods=['POST'])
def chat_api():
    try:
        question = request.json['question']
        chat_prompt = restaurant_data_prompt + f"\nQ: {question}\nA:"
        
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose the appropriate engine
            prompt=chat_prompt,
            max_tokens=50  # Adjust the number of tokens as needed
        )
        
        answer = response.choices[0].text.strip()
        return jsonify({"result": answer}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Order API
@app.route('/order', methods=['POST'])
def order_api():
    try:
        item_name = request.json['item_name']
        item_price = find_item_price(item_name)  # Implement your logic to find item price
        
        # Use ChatGPT for order confirmation
        order_confirmation = generate_order_confirmation(item_name, item_price)
        
        return jsonify({"result": order_confirmation}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Helper function to generate order confirmation message
def generate_order_confirmation(item_name, item_price):
    chat_prompt = f"Q: How much does {item_name} cost?\nA: {item_price}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the appropriate engine
        prompt=chat_prompt,
        max_tokens=50  # Adjust the number of tokens as needed
    )
    
    confirmation = response.choices[0].text.strip()
    return f"Order for item: {item_name}, price: {item_price} placed successfully. {confirmation}"

# Helper function (implement your own logic here)
def find_item_price(item_name):
    # This function should find and return the price of the item
    # from your restaurant menu data or database
    # Replace this with your actual logic
    menu = {
        "Grilled Salmon": "$18.50",
        "Pasta Alfredo": "$15.99",
        # Add more items
    }
    return menu.get(item_name, "Unknown")

if __name__ == '__main__':
    app.run(debug=True)
