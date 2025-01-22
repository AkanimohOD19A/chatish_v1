from chat_manager import ChatManager
from file_handler import FileHandler
import streamlit as st


def initialize_app():
    st.set_page_config(page_title="Tabular Chatish", layout="wide")
    st.title("Chatish")
    st.subheader("A demonstration chatbots with contextual retrieval")

    if 'messages' not in st.session_state:
        st.session_state.messages = []

## pages-subdir:
# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def setup_sidebar():
    with st.sidebar:
        api_key = st.text_input("Enter your Cohere API Key", type="password")
        st.link_button("Get one @ Cohere 🔗", "https://dashboard.cohere.com/api-keys")
        if not api_key:
            st.warning("Please enter a valid COHERE API-KEY")

            return None, None

        st.markdown("")
        st.markdown("")

        uploaded_file = st.file_uploader("Choose a file for additional context - PDFs, CSV")
        file_content = None
        if uploaded_file:
            file_handler = FileHandler()
            file_content = file_handler.process_file(uploaded_file)

            preview_options = ['Fine preview', 'Raw text', None]
            preview_selection = st.segmented_control(
                "View uploaded file as",
                preview_options,
                selection_mode="single"
            )

            if preview_selection:
                file_handler.show_preview(
                    preview_selection,
                    file_content,
                    uploaded_file
                )

        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.write("Made with ❤️ by [Akan](https://akanimohod19a.github.io/)")

        return api_key, file_content

def main():
    initialize_app()
    api_key, file_content = setup_sidebar()

    if not api_key:
        return

    chat_manager = ChatManager(api_key)

    # Display chat history
    st.markdown("### 💬 Conversation History")
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.text(message["content"])

    # Handle user input
    if prompt := st.chat_input("What do you think about this?"):
        chat_manager.add_user_message(prompt)

        with st.chat_message("assistant"):
            response = chat_manager.get_bot_response(prompt, file_content)
            chat_manager.add_assistant_message(response)

    # Clear chat button
    if st.session_state.messages:
        st.button("Clear ↺", on_click=chat_manager.reset_chat)


if __name__ == "__main__":
    main()