#!/usr/bin/env python3
"""
Orquestrador de Execução - FSV-Core API
Inicia o servidor determinístico em ambiente local ou de produção.
"""

import sys
import os

# Garante que a pasta src está no caminho de execução do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

try:
    import uvicorn
    from src.api import app
except ImportError as e:
    print(f"[Erro Crítico] Dependência faltando: {e}")
    print("Execute: pip install -r requirements_api.txt")
    sys.exit(1)

if __name__ == "__main__":
    print("==================================================")
    print("  FSV-Core: Iniciando Motor Híbrido de API...   ")
    print("  Documentação Swagger disponível em: /docs       ")
    print("==================================================")
    
    # Executa o servidor na porta padrão local
    uvicorn.run("src.api:app", host="127.0.0.1", port=8000, reload=True)
