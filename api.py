#!/usr/bin/env python3
"""
Módulo de API Gateway (FSV-Core API)
Expõe o motor matemático e a busca determinística via HTTP.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from validator import DataSanitizer
from src.analyzer import AdvancedSignatureAnalyzer, comparar_metricas
from database_mock import SignatureDatabaseMock

app = FastAPI(
    title="FSV-Core API",
    description="Motor Híbrido de Triagem Forense e Proveniência",
    version="2.0"
)

class AnaliseRequest(BaseModel):
    autor_chave: str
    amostra_matriz: List[List[int]]

@app.post("/auditar")
def auditar_assinatura(payload: AnaliseRequest):
    # 1. Validação estrita de entrada
    validacao = DataSanitizer.validar_matriz_assinatura(payload.amostra_matriz)
    if not validacao["valido"]:
        raise HTTPException(status_code=400, detail=validacao["erro"])
    
    # 2. Busca determinística no banco de referência
    db = SignatureDatabaseMock()
    registro = db.buscar_referencia(payload.autor_chave)
    if registro["status"] == "erro":
        raise HTTPException(status_code=404, detail=registro["mensagem"])
    
    metrica_ref = registro["metrica_padrao"]

    # 3. Processamento matemático
    analisador = AdvancedSignatureAnalyzer(payload.amostra_matriz)
    metrica_teste = analisador.compute_geometric_metrics()
    
    score = comparar_metricas(metrica_ref, metrica_teste)
    
    parecer = "Alta compatibilidade com o Dataset de Ouro." if score >= 90.0 else "Divergência estrutural detectada."

    return {
        "autor": registro["autor"],
        "periodo": registro["periodo"],
        "indice_compatibilidade": score,
        "parecer_preliminar": parecer,
        "status": "sucesso"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
