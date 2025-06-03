# file_processing.py

import io
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
import docx2txt
import streamlit as st

def extract_text_from_file(uploaded_file):
    file_name = uploaded_file.name.lower()
    text = ""

    if file_name.endswith('.txt'):
        try:
            content = uploaded_file.read()
            encoding = 'utf-8'
            text = content.decode(encoding)
        except UnicodeDecodeError:
            st.warning("Trying 'latin-1' encoding.")
            try:
                text = content.decode('latin-1')
            except UnicodeDecodeError as e:
                st.error(f"Error decoding text file: {e}")
    elif file_name.endswith('.pdf'):
        try:
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                text += page.extract_text() or ''
        except Exception as e:
            st.error(f"Error reading PDF file: {e}")
    elif file_name.endswith('.docx'):
        try:
            text = docx2txt.process(uploaded_file)
        except Exception as e:
            st.error(f"Error reading DOCX file: {e}")
    else:
        st.warning("Unsupported file type. Please upload a .txt, .pdf, or .docx file.")
    return text

def extract_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        for script in soup(["script", "style", "header", "footer", "nav", "aside"]):
            script.decompose()
        text = soup.get_text(separator=' ')
        text = ' '.join(text.split())
        return text
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching URL: {e}")
        return ""

