import streamlit as st
from huggingface_hub import InferenceClient

# Initialize InferenceClient 
client = InferenceClient(
    provider="cohere",
    api_key=st.secrets["hf_token"],  
)

# Define the system prompt for the chatbot
system_prompt = """أنت مساعد دردشة لمتجر إلكتروني خليجي. تحدث بلغة عربية بسيطة وبأسلوب إماراتي ودود، وساعد المستخدم بسرعة ووضوح."""
 
# Function to generate a response based on user input
def get_chat_response(user_input):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input},
    ]
    completion = client.chat.completions.create(
        model="CohereLabs/c4ai-command-r7b-arabic-02-2025",
        messages=messages,
        max_tokens=512,
    )
    return completion.choices[0].message.content

# Streamlit interface
st.title("Gulf chatbot demo")  

user_input = st.text_input("أهلاً! كيف يمكنني مساعدتك؟")

if user_input:
    response = get_chat_response(user_input)
    st.write(response)
