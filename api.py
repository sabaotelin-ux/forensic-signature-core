from fastapi import FastAPI, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List
import os

app = FastAPI(
    title="API de Análise de Assinatura",
    version="1.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnaliseRequest(BaseModel):
    autor_chave: str = Field(..., example="exemplo")
    amostra_matriz: List[List[int]] = Field(
        ...,
        example=[
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    )

@app.get("/")
def home():
    if os.path.exists("index.html"):
        return FileResponse("index.html")
    return {"status": "on-line", "docs": "/docs"}

@app.get("/saude")
def saude():
    return {"status": "OK"}

@app.get("/autores")
def listar_autores():
    # Você precisa ter a classe AssinaturaDatabaseMock definida
    db = AssinaturaDatabaseMock()
    return {"autores_disponiveis": db.listar()}

@app.post("/auditor")
def auditar_assinatura(carga_util: AnaliseRequest):
    # Você precisa ter a classe DataSanitizer definida
    validacao = DataSanitizer.validar_matriz(carga_util.amostra_matriz)
    
    if not validacao["valido"]:
        return {"erro": "Matriz inválida", "detalhes": validacao}
