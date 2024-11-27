# backend.py
import google.generativeai as genai
import streamlit as st

gemini_api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
    }
)

def GenerateResponse(input_text):
    try:
        response = model.generate_content([
            "answer all questions as possible",
            "input: who are you?",
            "output: I'm the BND CHATBOT",
            "input: what all you can do?",
            "output: i can help by answering your inquiries",
            f"input: {input_text}",
            "output: ",
        ])
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"
