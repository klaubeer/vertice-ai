"""
Configurações centrais do Vértice IA.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# ============================================
# Caminhos
# ============================================
RAIZ_PROJETO = Path(__file__).parent.parent
CAMINHO_DADOS = RAIZ_PROJETO / "dados"
CAMINHO_DOCUMENTOS = CAMINHO_DADOS / "documentos"
CAMINHO_BANCO = RAIZ_PROJETO / os.getenv("CAMINHO_BANCO", "banco/vertice.db")
CAMINHO_CHROMA = RAIZ_PROJETO / os.getenv("CAMINHO_CHROMA", "banco/chroma_db")

# ============================================
# Anthropic / Claude
# ============================================
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
MODELO_CLAUDE = os.getenv("MODELO_CLAUDE", "claude-sonnet-4-20250514")

# ============================================
# RAG
# ============================================
MODELO_EMBEDDINGS = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
MODELO_RERANQUEADOR = "cross-encoder/ms-marco-MiniLM-L-6-v2"
TAMANHO_CHUNK = 512
SOBREPOSICAO_CHUNK = 64
TOP_K_RECUPERACAO = 10
TOP_K_RERANQUEAMENTO = 5
LIMIAR_CONFIANCA = float(os.getenv("LIMIAR_CONFIANCA", "0.7"))

# ============================================
# LangFuse (Observabilidade)
# ============================================
LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY", "")
LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY", "")
LANGFUSE_HOST = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")

# ============================================
# Empresa fictícia
# ============================================
NOME_EMPRESA = "Vértice"
LOJAS = [
    "Av. Paulista - SP",
    "Shopping Ibirapuera - SP",
    "Shopping Eldorado - SP",
    "Rua Oscar Freire - SP",
    "Shopping RioSul - RJ",
    "Barra Shopping - RJ",
    "Shopping Curitiba - PR",
    "BH Shopping - MG",
]
