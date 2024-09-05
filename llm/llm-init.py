from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import requests  # Ensure you have imported requests
# from ollama_llm import askllm
from lm_studio_llm import get_lm_studio_reponse, reset_history, check_if_LLM_live   # Import reset_history function

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

# Configure logging
logging.basicConfig(level=logging.INFO)  # Log level can be adjusted as needed
logger = logging.getLogger(__name__)

@app.before_request
def log_request_info():
    logger.info(f'Request Headers: {request.headers}')
    logger.info(f'Request URL: {request.url}')
    logger.info(f'Request Method: {request.method}')
    logger.info(f'Request Body: {request.get_data()}')

@app.route('/ask', methods=['POST'])
def ask_llm_route():
    data = request.get_json()
    user_prompt = data.get('prompt', '')
    if not user_prompt:
        logger.warning('Prompt is required but not provided')
        return jsonify({'error': 'Prompt is required'}), 400

    try:
        # Use the get_llm_response function to get the LLM response
        response_text = get_llm_response(user_prompt)
        logger.info(f'Response generated successfully')
        return jsonify({'response': response_text})
    except Exception as e:
        logger.error(f'Error in /ask endpoint: {str(e)}')
        return jsonify({'error': 'An error occurred'}), 500

@app.route('/reset_session', methods=['POST'])
def reset_session_route():
    try:
        # Call the reset_history function to reset the session
        reset_history()
        logger.info('Session reset successfully')
        return jsonify({'message': 'Session reset successfully'}), 200
    except Exception as e:
        logger.error(f'Error in /reset_session endpoint: {str(e)}')
        return jsonify({'error': str(e)}), 500

def get_llm_response(prompt):
    try:
        # lm_studio service
        response = get_lm_studio_reponse(prompt)
        return response  # Return the response content directly
    except requests.RequestException as e:
        logger.error(f'Error in get_llm_response: {str(e)}')
        return str(e)
    
@app.route('/checkLLM', methods=['POST'])
def check_llm_route():
    try:
        # Call the check_if_LLM_live function to check LLM status
        status = check_if_LLM_live()
        logger.info(f'LLM status checked: {status}')
        return jsonify({'status': status}), 200
    except Exception as e:
        logger.error(f'Error in /checkLLM endpoint: {str(e)}')
        return jsonify({'status': str(e)}), 500
        
@app.route('/pinger_response', methods=['GET'])
def pinger_response_route():
    return jsonify({'message': 'session is active'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5002)
