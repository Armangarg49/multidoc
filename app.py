#app.py

import streamlit as st
from utils import load_and_process_docs, answer_query  # your utils functions
st.write("Hello, Streamlit app is running!")
st.title("Multi-Document RAG Chatbot")

uploaded_files = st.file_uploader("Upload Documents", accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Processing documents..."):
        # Process documents to create vectorstore, embeddings
        vectorstore = load_and_process_docs(uploaded_files)

    query = st.text_input("Ask a question:")
    if query:
        with st.spinner("Generating answer..."):
            answer = answer_query(vectorstore, query)
            st.write("Answer:", answer)
