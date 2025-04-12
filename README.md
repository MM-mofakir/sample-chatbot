

## Description:
------------
This Python program implements a context-aware chatbot that answers user questions based on a set of documents.
It uses:
- LangChain for chaining language model and retriever,
- ChromaDB for storing and retrieving vector embeddings,
- SentenceTransformer for creating text embeddings,
- Ollama's LLaMA 3 model for generating responses.

## Dependencies:
-------------
- langchain
- langchain_community
- chromadb
- ollama
- sentence-transformers

## Main Components:
----------------

1. # add_documents(docs):
    Adds a list of text documents to the ChromaDB vector store.
    Converts each document into a vector using SentenceTransformer embeddings.

2. # get_chatbot_response(query):
    Handles user queries by:
    - Retrieving the most relevant documents from the vector store,
    - Passing the documents and query to a RetrievalQA chain powered by the LLaMA 3 model,
    - Returning a context-aware response.

## Main Execution:
---------------
- Initializes embedding function and ChromaDB persistent client.
- Loads or creates a Chroma collection named "chatbot_knowledge".
- Loads the LLaMA 3 model via Ollama.
- Adds predefined context documents to the vector store.
- Runs a chat loop where the user can enter queries and receive answers.
  Type "exit" or "quit" to stop the program.

## Example Context Documents:
--------------------------
- Machine learning basics
- Meta’s LLaMA models
- ChromaDB description

Usage:
------
Run the script, type a question, and receive AI-generated answers based on stored knowledge.

"""
pip install virtualenv
virtualenv env
env/Scripts/activate
python -m pip install -r requirements.txt
python chatbot.py







