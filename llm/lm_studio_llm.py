from openai import OpenAI
history = [
            {"role": "assistant", "content": "Always answer in very brief."}
        ]

# Initialize the OpenAI client
api_key: str = "lm-studio"
# base_url: str = "http://localhost:1234/v1" # just in case if llm-server needs to be locally hosted and use llm directly
base_url: str = "https://sure-tightly-asp.ngrok-free.app/v1"
client = OpenAI(base_url=base_url, api_key=api_key)

# Function to interact with OpenAI
def get_lm_studio_reponse(prompt: str, model: str = "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF",):

    history.append({"role": "user", "content": prompt})

    # Create the completion request
    completion = client.chat.completions.create(
        model=model,
        # messages=[
        #     {"role": "system", "content": "Always answer in very brief."},
        #     {"role": "user", "content": prompt}
        # ],
        messages=history,
        temperature=0.7,
    )
    
    #append into history
    history.append({"role": "assistant", "content": completion.choices[0].message.content})
    # Return the response
    return completion.choices[0].message.content

# Function to reset the history
def reset_history():
    global history
    history = [{"role": "assistant", "content": "Always answer in very brief."}]

def check_if_LLM_live(model: str = "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF"):
    try:
        # Define a minimal prompt to check if the LLM is live
        test_prompt = [
            {"role": "user", "content": "Always answer in very brief."}
        ]
        
            # Create the completion request
        completion = client.chat.completions.create(
            model=model,
            # messages=[
            #     {"role": "system", "content": "Always answer in very brief."},
            #     {"role": "user", "content": prompt}
            # ],
            messages=test_prompt,
            temperature=0.7,
        )
        
        response = completion.choices[0].message.content
        # Check if the response is valid or contains an expected result
        if response:
            return "LLM is live"
        else:
            return "LLM is down"
    
    except Exception as e:
        # Log the exception if needed (optional)
        print(f"Exception occurred: {e}")
        # Return a message indicating the LLM is down
        return "LLM is down"