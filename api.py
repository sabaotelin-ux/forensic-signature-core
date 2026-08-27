#!/usr/bin/env python3
"""
FSV-Core API - Motor Híbrido de Triagem Forense e Proveniência
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from typing import List
import os

from validator import DataSanitizer
from src.analyzer import AdvancedSignatureAnalyzer, comparar_metricas
from database_mock import SignatureDatabaseMock

app = FastAPI(
    title="FSV-Core API",
    description="Motor Híbrido de Triagem Forense e Proveniência de Assinaturas",
    version="2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnaliseRequest(BaseModel):
    autor_chave: str = Field(..., example="portinari_1950")
    amostra_matriz: List[List[int]] = Field(
        ...,
        example=[
            [0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,1,0,0,1,0,0],
            [0,0,1,0,0,0,1,1,1,0],
            [0,0,1,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
    )

@app.get("/")
def home():
    if os.path.exists("index.html"):
        return FileResponse("index.html")
    return {"status": "online", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/autores")
def listar_autores():
    db = SignatureDatabaseMock()
    return {"autores_disponiveis": db.listar_autores_disponiveis()}

@app.post("/auditar")
def auditar_assinatura(payload: AnaliseRequest):
    validacao = DataSanitizer.validar_matriz_assinatura(payload.amostra_matriz)
    if not validacao["valido"]:
        raise HTTPException(status_code=400, detail=validacao["erro"])
    
    db = SignatureDatabaseMock()
    registro = db.buscar_referencia(payload.autor_chave)
    if registro["status"] == "erro":
        raise HTTPException(status_code=404, detail=
