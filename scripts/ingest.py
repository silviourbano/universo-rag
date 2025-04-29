# scripts/ingest.py
import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

DATA_DIR = "data/raw"
INDEX_DIR = "data/index"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def load_documents():
    loaders = [
        # PyPDFLoader(os.path.join(DATA_DIR, "procedimento_redes.pdf")),
        # TextLoader(os.path.join(DATA_DIR, "tcping_link.txt"))
        TextLoader(os.path.join(DATA_DIR, "venda_de_bolos.txt"))
    ]
    documents = []
    for loader in loaders:
        documents.extend(loader.load())
    return documents

def main():
    print("📄 Carregando documentos...")
    docs = load_documents()

    print("✂️  Separando documentos...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    print("📐 Gerando embeddings...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

    print("🧠 Criando índice FAISS...")
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(INDEX_DIR)

    print("✅ Indexação finalizada!")

if __name__ == "__main__":
    main()
