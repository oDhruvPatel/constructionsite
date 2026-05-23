import streamlit as st
from src.helper import get_pdf, get_chunks, create_vector_store, get_convo_chain

def user_input(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chatHistory = response['chat_history']
    for i, message in enumerate(st.session_state.chatHistory):
        if i%2 == 0:
            st.write("User: ", message.content)
        else:
            st.write("AI: ", message.content)

def main():
    st.set_page_config("Information retrieval")
    st.header("Information retrieval system")
    
    user_question = st.text_input("Ask Question from your pdf files")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
        
    if user_question:
        if st.session_state.conversation is not None:
            user_input(user_question)
        else:
            st.warning("Please upload and process a PDF file first before asking questions.")

    with st.sidebar:
        st.title("Menu")
        pdf_docs = st.file_uploader("Upload PDF Files and Click on the Submit Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                 
                pdf_text = get_pdf(pdf_docs)
                text_chunks = get_chunks(pdf_text)
                vector_store = create_vector_store(text_chunks)
                st.session_state.conversation = get_convo_chain(vector_store)
                st.success("Done")

if __name__ == "__main__":
    main()
