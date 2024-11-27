import streamlit as st
import google.generativeai as genai

# Set up your API key
gemini_api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=gemini_api_key)

# Create the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
    }
)

def generate_response(input_text):
    try:
        response = model.generate_content([
            "answer all questions as possible",
            "input: who are you?",
            "output: I'm the School Help Desk",
            "input: what all you can do?",
            "output: i can help by answering your inquiries",
            f"input: {input_text}",
            "output: ",
        ])
        return response.text
