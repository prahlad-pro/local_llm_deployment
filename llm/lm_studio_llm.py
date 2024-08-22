from openai import OpenAI

# Function to interact with OpenAI
def get_lm_studio_reponse(prompt: str, model: str = "model-identifier", api_key: str = "lm-studio", base_url: str = "http://localhost:1234/v1"):
    # Initialize the OpenAI client
    client = OpenAI(base_url=base_url, api_key=api_key)
    
    # Create the completion request
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Always answer in very brief."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    
    # Return the response
    return completion.choices[0].message.content

# Example usage
response = get_lm_studio_reponse("Introduce yourself.")
print(response)