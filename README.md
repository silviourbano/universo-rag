# 🤖 universo-rag

**universo-rag** é um projeto simples e poderoso de Recuperação Aumentada por Geração (RAG) rodando inteiramente de forma local.  
Você fornece seus próprios documentos — o sistema cuida de buscar o contexto e perguntar para o modelo LLM que você escolher.

---

## ✨ O que é isso?

Este repositório demonstra como montar uma base local de documentos com FAISS + LangChain, criar embeddings com modelos da HuggingFace e enviar perguntas para um LLM local via HTTP.

Use casos:
- Chat com PDFs, textos e bases próprias
- Assistentes locais que não dependem de nuvem pública
- Protótipos de IA conversacional com custo zero

---

## 📦 Instalação

Requisitos:
- Python 3.10+
- Ambiente virtual ativo (`venv`, `poetry`, etc.)

```bash
make install
```

---

## 🏗️ Indexação dos dados

Coloque seus arquivos de texto ou PDF em `data/raw/`.  
Este projeto já inclui um exemplo chamado `venda_de_bolos.txt`.

Para criar o índice FAISS:

```bash
make ingest
```

---

## 💬 Como usar

Execute o motor principal com:

```bash
make ask
```

Digite sua pergunta, e a IA responderá com base no conteúdo encontrado.

---

## 🧠 Prompt usado

Arquivo `app/prompt_template.txt`:

```
Você é assistente útil que responde perguntas sobre os produtos que vendemos.
Não responda perguntas que não sejam sobre os produtos.
Você deve responder com base nas informações que temos disponíveis.
Não invente informações que você não tem. Não faça perguntas.
Você deve responder de forma clara e objetiva, sem rodeios.
A resposta é sempre para um cliente.

Contexto:
{context}

{question}
```

---

## 📂 Estrutura do projeto

```text
.
├── app/                  # Engine principal e template de prompt
├── data/raw/            # Documentos brutos
├── data/index/          # Arquivos FAISS gerados
├── scripts/             # Scripts utilitários (ex: ingestão)
├── Makefile             # Atalhos de execução
├── requirements.txt     # Dependências
```

---

## 🔧 Comandos disponíveis

```bash
make install   # Instala dependências no ambiente virtual
make ingest    # Executa o script de indexação dos documentos
make ask       # Roda o RAG para responder perguntas
make clean     # Remove arquivos temporários e índice vetorial
```

---

## 🌐 Variáveis de ambiente (.env)

```env
CHAT_API_URL=http://localhost:5000/chat
```

---

## 🚀 Ideias futuras

- Suporte a PDF, MarkDown, CSV e HTML
- Interface com Streamlit
- Indexação incremental
- Histórico de perguntas

---

Criado com visão de autonomia, liberdade computacional e foco em experiências reais de uso.  
Vamos expandir esse universo local? 🌍