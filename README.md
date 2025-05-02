## 📁 Estrutura do repositório **universo-rag**

```
universo-rag/
├── app/                        # Código principal do app RAG
│   ├── rag_engine.py           # Pipeline RAG: embeddings + busca + envio para modelo
│   └── prompt_template.txt     # Template de prompt usado com o contexto
│
├── data/                       # Dados usados no RAG
│   ├── raw/                    # Documentos originais
│   │   └── venda_de_bolos.txt  # Informações sobre a loja e os produtos vendidos
│   └── index/                  # Arquivos do FAISS (índice vetorial)
│
├── scripts/                    # Scripts auxiliares
│   └── ingest.py               # Carrega e indexa os documentos em FAISS
│
├── requirements.txt            # Dependências do projeto
└── README.md                   # Instruções e visão geral do projeto
```
