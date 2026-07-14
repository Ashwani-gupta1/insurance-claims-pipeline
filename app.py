import streamlit as st

from src.ai.assistant import AIAssistant


st.set_page_config(
    page_title="Insurance Claims AI Assistant",
    page_icon="🤖"
)


st.title("🤖 Insurance Claims AI Assistant")

st.write(
    "Ask questions about your insurance claims warehouse"
)


# Initialize assistant
if "assistant" not in st.session_state:
    st.session_state.assistant = AIAssistant()


# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# User input
question = st.chat_input(
    "Ask about claims..."
)


if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    with st.chat_message("user"):
        st.write(question)


    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = st.session_state.assistant.ask(
                question
            )


            if hasattr(response, "empty"):

                st.dataframe(response)


                summary = (
                    st.session_state
                    .assistant
                    .explain(response)
                )

                st.write(
                    summary
                )

            else:

                st.write(response)


            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": str(response)
                }
            )