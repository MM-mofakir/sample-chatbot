import chromadb
import ollama
from langchain_chroma import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.schema import Document
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory




# Step 2: Function to Add Context Documents
def add_documents(docs):
    documents = [Document(page_content=doc) for doc in docs]
    vectorstore = Chroma(client=chroma_client, collection_name="chatbot_knowledge", embedding_function=embedding_function)
    vectorstore.add_documents(documents)
    print("Documents added successfully!")


# Step 4: Create Retrieval-based QA System
def get_chatbot_response(query):

    vectorstore = Chroma(client=chroma_client, collection_name="chatbot_knowledge", embedding_function=embedding_function)
    retriever = vectorstore.as_retriever()
    print(retriever,'==================================================================================================')
    qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type='stuff',
            retriever=retriever,
            verbose=True)
    response = qa_chain(query)
    # response = ollama(prompt)
    # return response
    
    print(qa_chain,'==========================================qa_chain========================================================')
    response = qa_chain.run(query)
  
    return response



if __name__ == '__main__':
    
   embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
   chroma_client = chromadb.PersistentClient(path="./chroma_db")
   collection = chroma_client.get_or_create_collection(name="chatbot_knowledge")

    # Step 3: Load Llama Model (Ollama)
   llm = Ollama(model="llama3")


    # Step 5: Add Sample Context
  context_docs = [
    "Machine learning is a subset of artificial intelligence that enables computers to learn from data.",
    "Llama models are developed by Meta and are optimized for local AI applications.",
    "ChromaDB is a powerful vector database for storing and retrieving embeddings efficiently."
   ]
  add_documents(context_docs)

   # Step 6: Run the Chatbot
  print("Chatbot is ready! Type your question.")

  while True:
    user_query = input("You: ")
    if user_query.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    response = get_chatbot_response(user_query)
    print("Chatbot:", response)
