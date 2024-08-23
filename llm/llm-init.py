from flask import Flask, request, jsonify
from flask_cors import CORS
import requests  # Ensure you have imported requests
# from ollama_llm import askllm
from lm_studio_llm import get_lm_studio_reponse

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

@app.route('/ask', methods=['POST'])
def ask_llm_route():
    data = request.get_json()
    user_prompt = data.get('prompt', '')
    if not user_prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    # Use the askllm function to get the LLM response
    response_text = get_llm_response(user_prompt)
    return jsonify({'response': response_text})

def get_llm_response(prompt):
    try:
        # ollama service
        # response = askllm(prompt)
        # lm_studio service
        response = get_lm_studio_reponse(prompt)
        return response  # Return the response content directly
    except requests.RequestException as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True, port=5002)