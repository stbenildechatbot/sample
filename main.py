import streamlit as st
import time
import backend

def response_generator(prompt):
    try:
        response = backend.GenerateResponse(prompt)
        lines = response.split('\n')
        for line in lines:
            words = line.split()
            for word in words:
                yield word + " "
                time.sleep(0.05)
            yield "\n"  # Preserve line breaks
    except Exception as e:
        yield f"An error occurred: {str(e)}"

# Callback for recommended question buttons
def ask_recommended_question(question):
    st.session_state.messages.append({"role": "user", "content": question})

st.title("BND CHATBOT")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("HI! I'm BND Chatbot, what is your question?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

# After displaying chat history and handling chat input,
# check if the last message is from the user and generate a response
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    prompt = st.session_state.messages[-1]["content"]
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    st.session_state.messages.append({"role": "assistant", "content": response})

# Add recommended question buttons
st.write("Recommended questions:")
col1, col2 = st.columns(2)
with col1:
    st.button("What programs do you offer?", on_click=ask_recommended_question, kwargs={"question": "What programs do you offer?"})
    st.button("How can I contact support?", on_click=ask_recommended_question, kwargs={"question": "How can I contact support?"})
with col2:
    st.button("Tell me about your pricing", on_click=ask_recommended_question, kwargs={"question": "Tell me about your pricing"})
    st.button("What are your business hours?", on_click=ask_recommended_question, kwargs={"question": "What are your business hours?"})
