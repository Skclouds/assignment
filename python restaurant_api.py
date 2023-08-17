from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Mock restaurant data for system prompt
restaurant_data = """
Restaurant Menu:
1. Burger - $10
2. Pizza - $12
3. Salad - $8
Location: 123 Main St.
Welcome to our restaurant! How can I assist you today?
"""

# ChatGPT API endpoint and your ChatGPT API key
chatgpt_endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"
chatgpt_api_key = "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"

@app.route('/chat', methods=['POST'])
def chat_api():
    try:
        data = request.json
        question = data['question']

        # Construct prompt for ChatGPT
        prompt = f"{restaurant_data}\nUser: {question}\nAssistant:"

        # Call ChatGPT API
        response = requests.post(chatgpt_endpoint,
                                 json={"prompt": prompt},
                                 headers={"Authorization": f"Bearer {chatgpt_api_key}"}).json()

        result = response['choices'][0]['text'].strip()
        return jsonify({'result': result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/order', methods=['POST'])
def order_api():
    try:
        data = request.json
        item_name = data['item_name']

        # Mock item price lookup (you can replace this with actual logic)
        item_prices = {
            'Burger': 10,
            'Pizza': 12,
            'Salad': 8
        }

        item_price = item_prices.get(item_name, None)
        if item_price is None:
            return jsonify({'result': f"Item '{item_name}' not found"}), 404

        return jsonify({'result': f"Order for item: {item_name}, price: ${item_price} placed successfully"}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
