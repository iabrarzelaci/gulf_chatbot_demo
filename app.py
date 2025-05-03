from huggingface_hub import InferenceClient
import streamlit as st

client = InferenceClient(
    provider="cohere",
  api_key= st.secrets["hf_token"],
)

# Define the initial system prompt
system_prompt = """أنت مساعد دردشة لمتجر إلكتروني خليجي. تحدث بلغة عربية بسيطة وبأسلوب إماراتي ودود، وساعد المستخدم بسرعة ووضوح.
"""

# Initialize the chat history
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "سلام"}  # The first user query
]

# Make the API call with the chat history
completion = client.chat.completions.create(
    model="CohereLabs/c4ai-command-r7b-arabic-02-2025",
    messages=messages,
    max_tokens=512,
)

# Print the assistant's response
print(completion.choices[0].message)

# Example of continuing the conversation with new user input
messages.append({"role": "assistant", "content": completion.choices[0].message.content})  # Adding ONLY the content to history
messages.append({"role": "user", "content": "طلبي وايد تاخر"})  # New user query

# Make another API call to continue the conversation
completion = client.chat.completions.create(
    model="CohereLabs/c4ai-command-r7b-arabic-02-2025",
    messages=messages,
    max_tokens=512,
)

# Print the new assistant response
print(completion.choices[0].message)