#!/usr/bin/env python3
"""
FSV-Core API - Motor Híbrido de Triagem Forense e Proveniência
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List

from validator import DataSanitizer
from src.analyzer import AdvancedSignatureAnalyzer, comparar_metricas
from database_mock import SignatureDatabaseMock

app = FastAPI(
    title="FSV-Core API",
    description="Motor Híbrido de Triagem Forense e Proveniência de Assinaturas",
    version="2.0",
    contact={
        "name": "FSV-Core",
        "url": "https://github.com/sabaotelin-ux/forensic-signature-core"
    }
)

# Libera CORS (permite frontend acessar a API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnaliseRequest(BaseModel):
    autor_chave: str = Field(..., example="portinari_1950", description="Chave do autor de referência")
    amostra_matriz: List[List[int]] = Field(
        ..., 
        example=[
            [0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,1,0,0,1,0,0],
            [0,0,1,0,0,0,1,1,1,0],
            [0,0,1,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ],
        description="Matriz binária da assinatura (0 = fundo, 1 = traço)"
    )

@app.get("/")
def home():
    return {
        "nome": "FSV-Core API",
        "versao": "2.0",
        "descricao": "Motor Híbrido de Triagem Forense e Proveniência de Assinaturas",
        "documentacao": "/docs",
        "status": "online"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/autores")
def listar_autores():
    db = SignatureDatabaseMock()
    return {
        "autores_disponiveis": db.listar_autores_disponiveis()
    }

@app.post("/auditar")
def auditar_assinatura(payload: AnaliseRequest):
    # 1. Validação
    validacao = DataSanitizer.validar_matriz_assinatura(payload.amostra_matriz)
    if not validacao["valido"]:
        raise HTTPException(status_code=400, detail=validacao["erro"])
    
    # 2. Busca no banco de referência
    db = SignatureDatabaseMock()
    registro = db.buscar_referencia(payload.autor_chave)
    if registro["status"] == "erro":
        raise HTTPException(status_code=404, detail=registro["mensagem"])
    
    metrica_ref = registro["metrica_padrao"]

    # 3. Análise geométrica
    analisador = AdvancedSignatureAnalyzer(payload.amostra_matriz)
    metrica_teste = analisador.compute_geometric_metrics()
    
    score = comparar_metricas(metrica_ref, metrica_teste)
    
    parecer = (
        "Alta compatibilidade com o Dataset de Ouro." 
        if score >= 90.0 
        else "Divergência estrutural detectada."
    )

    return {
        "autor": registro["autor"],
        "periodo": registro["periodo"],
        "indice_compatibilidade": score,
        "parecer_preliminar": parecer,
        "status": "sucesso"
    }
