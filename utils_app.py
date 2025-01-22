import streamlit as st
from cohere import ClientV2
from PyPDF2 import PdfReader





def chunk_text(text, chunk_size=2000):
    """Split text into chunks"""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def reset_chat():
    st.session_state.messages = []
    st.rerun


class ContextAnalyzer:
    def __init__(self,
                 model="command-r-plus-08-2024",
                 max_tokens=500,
                 temperature=0.7):
        # self.client = ClientV2(api_key=st.secrets['COHERE_API_KEY'])
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.conversation_history = []
        self.data_context = {}

    def extract_text(pdf_pth):
        pdf_file = PdfReader(pdf_pth)
        pdf_text = "\n".join(page.extract_text() for page in pdf_file.pages)

        return pdf_text

    def build_context(self, df):
        """Build comprehensive context based off the resources"""
        context_str = "SALARY RECORDS INGESTED CONTEXT: \n\n"

        return context_str

    def get_response(self, user_credentials, user_input, pdf_pth=None):
        try:
            if pdf_pth is not None:
                context = self.extract_text(pdf_pth)
            else:
                context = ""
                no_response_msg = "No data context available."

            # Full Prompt
            full_prompt = (f"{context}\n\n"
                           f"Question: {user_input}"
                           f"Provide straight to the point response except when told"
                           f"to elaborate using available metrics and historical data")

            # System message
            system_message = """
            You are an intelligent system specialized in human chat interaction,
            interpersonal interactions and can guide on complex ideas.
            Consider all available metrics, trends, and patterns in your analysis.
            Make connections between different points to provide deeper insights.
            Support your analysis with specific numbers and trends.
            """

            co = ClientV2(user_credentials)
            print(user_credentials)
            response = co.chat(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                messages=[
                    {"role": "system", "content": system_message},
                    {
                        "role": "user",
                        "content": {full_prompt}
                    }
                ]
            )

            # Extract response text
            assistant_reply = response.message.content[0].text

            # Update conversation history
            self.conversation_history.append({"role": "user", "content": user_input})
            self.conversation_history.append({"role": "assistant", "content": assistant_reply})

            # Maintain history within length
            if len(self.conversation_history) > 10:
                self.conversation_history = self.conversation_history[-10:]

            return assistant_reply
        except Exception as e:
            return f"Error generating response: {str(e)}"

    def chat(self, user_credentials, user_input, pdf_pth):
        try:
            return self.get_response(user_credentials, user_input, pdf_pth)
        except Exception as e:
            return f"Error processing request: {str(e)}"
