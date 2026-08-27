from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from auditor import FolgaAuditor

app = FastAPI(
    title="FSV-Audit",
    description="Motor Híbrido de Auditoria e Detecção de Folgas em Respostas de IA",
    version="1.0.0"
)

auditor = FolgaAuditor()

class TextoRequest(BaseModel):
    texto: str
    origem: str = "desconhecida"  # opcional: chatgpt, claude, grok, etc.

@app.get("/")
def home():
    return {
        "status": "online",
        "servico": "FSV-Audit",
        "versao": "1.0.0",
        "docs": "/docs"
    }

@app.get("/saude")
def saude():
    return {"status": "OK"}

@app.post("/auditar")
def auditar_resposta(payload: TextoRequest):
    if not payload.texto or len(payload.texto.strip()) < 10:
        raise HTTPException(status_code=400, detail="Texto muito curto para auditoria")

    resultado = auditor.auditar(payload.texto)
    resultado["origem_informada"] = payload.origem

    return resultado
