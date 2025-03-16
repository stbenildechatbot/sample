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

# Callback function for recommendation buttons
def ask_recommended_question(question):
    st.session_state.messages.append({"role": "user", "content": question})
    # This will trigger a rerun, and the prompt will be processed in the next run

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
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Add recommended question buttons
st.write("Recommended questions:")
col1, col2 = st.columns(2)
with col1:
    st.button("What services do you offer?", on_click=ask_recommended_question, 
              kwargs={"question": "What services do you offer?"})
    st.button("How can I contact support?", on_click=ask_recommended_question, 
              kwargs={"question": "How can I contact support?"})
with col2:
    st.button("Tell me about your pricing", on_click=ask_recommended_question, 
              kwargs={"question": "Tell me about your pricing"})
    st.button("What are your business hours?", on_click=ask_recommended_question, 
              kwargs={"question": "What are your business hours?"})
