import openai

# Set up OpenAI API credentials
openai.api_key = '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'

# Define a conversation
conversation = [
    {"role": "user", "content": "Hello, how are you?"},
    {"role": "assistant", "content": "I'm good, thank you! How can I assist you today?"}
]

# Send a message and receive a response
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation
)

# Extract the assistant's reply
reply = response['choices'][0]['message']['content']
print("Assistant:", reply)
