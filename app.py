import streamlit as st
from huggingface_hub import InferenceClient

# Initialize InferenceClient 
client = InferenceClient(
    provider="cohere",
    api_key=st.secrets["hf_token"],  
)

# Define the initial system prompt
system_prompt = """أنت مساعد دردشة لمتجر إلكتروني خليجي. تحدث بلغة عربية بسيطة وبأسلوب إماراتي ودود، وساعد المستخدم بسرعة ووضوح.
"""

# Initialize the chat history
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "سلام"}  # The first user query
]

# Function to handle chat responses
def get_chat_response(user_input):
    global messages
    # Append new user message to history
    messages.append({"role": "user", "content": user_input})
    
    # Make the API call to get the response
    completion = client.chat.completions.create(
        model="CohereLabs/c4ai-command-r7b-arabic-02-2025",
        messages=messages,
        max_tokens=512,
    )
    
    # Get the assistant's response
    assistant_response = completion.choices[0].message.content
    # Append assistant's response to history
    messages.append({"role": "assistant", "content": assistant_response})
    
    return assistant_response

# Streamlit interface
st.title("Gulf chatbot demo")  

user_input = st.text_input("أهلاً! كيف يمكنني مساعدتك؟")

if user_input:
    response = get_chat_response(user_input)
    st.write(response)
