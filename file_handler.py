import tempfile
from PyPDF2 import PdfReader
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer


class FileHandler:
    @staticmethod
    def extract_text_from_pdf(pdf_file):
        pdf_reader = PdfReader(pdf_file)
        return "\n".join(page.extract_text() for page in pdf_reader.pages)

    def process_file(self, uploaded_file):
        if uploaded_file.type == "application/pdf":
            return self.extract_text_from_pdf(uploaded_file)
        else:
            # Add handlers for other file types (CSV, etc.) here
            return uploaded_file.read().decode()

    def show_preview(self, preview_type, content, original_file):
        if preview_type == "Raw text":
            st.write(content)
        elif preview_type == "Fine preview":
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                tmp_file.write(original_file.getvalue())
                pdf_viewer(tmp_file.name)
