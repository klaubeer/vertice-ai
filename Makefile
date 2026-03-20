.PHONY: run indexar avaliar testes limpar instalar docker

# Instalar dependências
instalar:
	pip install -r requirements.txt

# Inicializar banco e indexar documentos
inicializar:
	python -m banco.inicializador
	python -m rag.indexador

# Indexar documentos no RAG
indexar:
	python -m rag.indexador

# Executar aplicação
run:
	streamlit run interface/app.py

# Rodar avaliação do RAG
avaliar:
	python -m avaliacao.avaliar_rag

# Rodar testes
testes:
	pytest testes/ -v

# Limpar banco e índices
limpar:
	rm -f banco/vertice.db
	rm -rf banco/chroma_db

# Docker
docker:
	docker-compose up --build

docker-parar:
	docker-compose down
