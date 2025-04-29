# app/rag_engine.py
import os
import requests
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

INDEX_DIR = "data/index"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHAT_URL = os.getenv("CHAT_API_URL", "http://localhost:5000/chat")

def build_prompt(context, question):
    with open("app/prompt_template.txt") as f:
        template = f.read()
    return template.replace("{context}", context).replace("{question}", question)

def main():
    question = input("❓ Sua pergunta: ")

    print("🔍 Buscando contexto...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    db = FAISS.load_local(INDEX_DIR, embeddings, allow_dangerous_deserialization=True)
    docs = db.similarity_search(question, k=6)
    context = "\n\n".join([d.page_content for d in docs])

    prompt = build_prompt(context, question)

    print("🤖 Enviando para o modelo...\n💬 Resposta:")
    try:
        # print(f"(ℹ️ prompt length: {len(prompt)} tokens aprox.)")
        with requests.post(CHAT_URL, json={"message": prompt}, stream=True, timeout=600) as response:
            response.raise_for_status()
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    print(chunk.decode("utf-8"), end="", flush=True)
        print("\n✅ Concluído.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao conectar com o modelo: {e}")

if __name__ == "__main__":
    main()
