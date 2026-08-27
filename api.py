from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
import os

# Imports dos módulos do projeto
from src.analyzer import AdvancedSignatureAnalyzer, comparar_metricas
from database_mock import SignatureDatabaseMock

app = FastAPI(
    title="FSV-Core API",
    description="Motor de Análise Forense de Assinaturas",
    version="2.0"
)

class AnaliseRequest(BaseModel):
    autor_chave: str
    amostra_matriz: List[List[int]]


@app.get("/")
def home():
    if os.path.exists("index.html"):
        return FileResponse("index.html")
    return {"status": "online", "docs": "/docs"}


@app.get("/saude")
def saude():
    return {"status": "OK"}


@app.get("/autores")
def listar_autores():
    db = SignatureDatabaseMock()
    return {"autores_disponiveis": db.listar_autores_disponiveis()}


@app.post("/auditar")
def auditar_assinatura(payload: AnaliseRequest):
    # Busca referência
    db = SignatureDatabaseMock()
    registro = db.buscar_referencia(payload.autor_chave)
    
    if registro.get("status") == "erro":
        raise HTTPException(status_code=404, detail=registro["mensagem"])
    
    # Análise geométrica
    analisador = AdvancedSignatureAnalyzer(payload.amostra_matriz)
    metrica_teste = analisador.compute_geometric_metrics()
    
    if metrica_teste.get("status") == "erro":
        raise HTTPException(status_code=400, detail=metrica_teste["mensagem"])
    
    # Comparação
    metrica_ref = registro["metrica_padrao"]
    score = comparar_metricas(metrica_ref, metrica_teste)
    
    parecer = (
