try:
    from langchain_community.vectorstores import FAISS
    from langchain_community.embeddings import FakeEmbeddings

    embedding = FakeEmbeddings(size=128)
    memory_db = FAISS.from_texts(["init"], embedding)

except Exception:
    memory_db = None

def save_memory(text):
    if memory_db:
        try:
            memory_db.add_texts([text])
        except:
            pass

def retrieve_memory(query):
    if memory_db:
        try:
            docs = memory_db.similarity_search(query, k=2)
            return "\n".join([d.page_content for d in docs])
        except:
            return ""
    return ""