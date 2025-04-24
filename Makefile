# Caminho para o ambiente virtual
VENV_DIR=.venv
PYTHON=$(VENV_DIR)/bin/python
PIP=$(VENV_DIR)/bin/pip

# Default: mostra os comandos disponíveis
.PHONY: help
help:
	@echo "Comandos disponíveis:"
	@echo "  make install         - Instala dependências no ambiente virtual"
	@echo "  make ingest          - Executa o script de ingestão (indexação dos documentos)"
	@echo "  make ask             - Roda o RAG para responder perguntas (exemplo interativo)"
	@echo "  make clean           - Remove arquivos gerados (índice, __pycache__...)"

.PHONY: install
install:
	$(PIP) install -r requirements.txt

.PHONY: ingest
ingest:
	$(PYTHON) scripts/ingest.py

.PHONY: ask
ask:
	$(PYTHON) app/rag_engine.py

.PHONY: clean
clean:
	rm -rf __pycache__ data/index/* .pytest_cache
