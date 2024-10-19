import os
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyAqip1JqptAc9n7l7JOKqOXDPvMJLDulf8")

# Set up the generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Load the generative model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

# Start a conversation
convo = model.start_chat(history=[])

# Send a prompt
response = convo.send_message("essay on AI")

# Print the response
print(response.text)
