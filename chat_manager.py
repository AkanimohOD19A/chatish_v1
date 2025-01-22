import streamlit as st
from cohere_client import CohereClient


class ChatManager:
    def __init__(self, api_key):
        self.cohere_client = CohereClient(api_key)

    def add_user_message(self, prompt):
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })
        with st.chat_message("user"):
            st.write(f"Prompt: {prompt}")

    def add_assistant_message(self, response):
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

    def get_bot_response(self, prompt, context=None):
        message_placeholder = st.empty()
        full_response = ""

        with st.spinner("Analyzing..."):
            response_chunks = self.cohere_client.chat(
                user_input=prompt,
                context=context
            )

            if isinstance(response_chunks, str):
                full_response = response_chunks
            else:
                for chunk in response_chunks:
                    full_response += chunk
                    message_placeholder.text(full_response + "▌")

        message_placeholder.text(full_response)
        return full_response

    @staticmethod
    def reset_chat():
        st.session_state.messages = []
        st.rerun()
