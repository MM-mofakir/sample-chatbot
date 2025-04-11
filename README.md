
"""
Chatbot using LangChain, ChromaDB, and Ollama (LLaMA 3)
## "interactive_chatbot"


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


## License
{license_text}
"""
MIT License

Copyright (c) 2021 MERZOUGUI Mahmoud

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.





