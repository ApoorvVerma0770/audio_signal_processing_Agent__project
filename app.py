from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Load knowledge base (sample data)
with open('knowledge_base.json', 'r') as f:
    knowledge_base = json.load(f)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# API route to handle user queries
@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.json.get('query', '').lower()
    response = "Sorry, I couldn't understand your query."

    for item in knowledge_base:
        if item['keyword'] in user_query:
            response = item['response']
            break

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)