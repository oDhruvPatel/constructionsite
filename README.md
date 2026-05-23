# Construction Site Document Q&A

A Retrieval-Augmented Generation (RAG) application that allows users to upload construction documents (PDFs) and ask questions about them. The system provides intelligent answers based on the uploaded content, including confidence scores and source citations to indicate exactly where the information came from.

## Features

- **Document Upload**: Upload multiple construction-related PDF documents.
- **Intelligent Q&A**: Ask natural language questions about the uploaded documents.
- **Confidence Scores**: Receive a confidence score indicating the reliability of the generated answer.
- **Source Tracking**: See exactly which part of the document the answer was extracted from.
- **Conversational Memory**: The AI remembers previous interactions for a seamless chat experience.

## Tech Stack

- **Frontend**: Streamlit
- **Language Model**: Google Gemini (`gemini-flash-latest`)
- **Embeddings**: Google Generative AI Embeddings (`models/gemini-embedding-2`)
- **Vector Database**: FAISS
- **Framework**: LangChain / LangChain-Google-GenAI

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/oDhruvPatel/constructionsite.git
   cd constructionsite
   ```

2. **Install dependencies:**
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your Google API key:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the application in your browser (usually `http://localhost:8501`).
2. Use the sidebar to upload one or more construction PDF documents.
3. Click on "Submit & Process" and wait for the documents to be processed into the vector database.
4. Once processed, type your questions in the main chat interface to get answers with confidence scores and source citations.
