from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings

embedding = FakeEmbeddings(size=128)

memory_db = FAISS.from_texts(["init"], embedding)

def save_memory(text):
    try:
        memory_db.add_texts([text])
    except:
        pass

def retrieve_memory(query):
    try:
        docs = memory_db.similarity_search(query, k=2)
        return "\n".join([d.page_content for d in docs])
    except:
        return ""