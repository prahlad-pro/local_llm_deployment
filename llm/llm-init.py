from flask import Flask, request, jsonify
from flask_cors import CORS
import requests  # Ensure you have imported requests
# from ollama_llm import askllm
from lm_studio_llm import get_lm_studio_reponse, reset_history, check_if_LLM_live   # Import reset_history function

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

@app.route('/reset_session', methods=['POST'])
def reset_session_route():
    try:
        # Call the reset_history function to reset the session
        reset_history()
        return jsonify({'message': 'Session reset successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_llm_response(prompt):
    try:
        # ollama service
        # response = askllm(prompt)
        # lm_studio service
        response = get_lm_studio_reponse(prompt)
        return response  # Return the response content directly
    except requests.RequestException as e:
        return str(e)
    
@app.route('/checkLLM', methods=['POST'])
def check_llm_route():
    try:
        # Call the check_if_LLM_live function to check LLM status
        status = check_if_LLM_live()
        return jsonify({'status': status}), 200
    except Exception as e:
        return jsonify({'status': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5002)