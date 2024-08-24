from openai import OpenAI
history = [
            {"role": "assistant", "content": "Always answer in very brief."}
        ]

# Initialize the OpenAI client
api_key: str = "lm-studio"
base_url: str = "http://localhost:1234/v1"
client = OpenAI(base_url=base_url, api_key=api_key)

# Function to interact with OpenAI
def get_lm_studio_reponse(prompt: str, model: str = "model-identifier",):

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

# Example usage
# response = get_lm_studio_reponse("Introduce yourself.")
# print(response)