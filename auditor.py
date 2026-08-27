import re
import hashlib
from datetime import datetime
from typing import List, Dict

class FolgaAuditor:
    """
    Motor Híbrido de Detecção de Folgas em respostas de IA.
    Camada 1: Determinística (regras + padrões clássicos de alucinação)
    """

    def __init__(self):
        self.padroes_suspeitos = [
            (r"\b(sempre|nunca|todos|nenhum|100%|absolutamente)\b", "Afirmação absoluta sem qualificação"),
            (r"\b(estudos mostram|pesquisas indicam|é fato que)\b(?!.*fonte)", "Afirmação genérica sem fonte"),
            (r"\b(em \d{4})\b", "Data específica (verificar se faz sentido no contexto)"),
            (r"\b(segundo a Wikipedia|de acordo com especialistas)\b", "Apelo vago a autoridade"),
        ]

    def auditar(self, texto: str) -> Dict:
        problemas = []
        score = 100

        # 1. Detecção de padrões suspeitos
        for padrao, descricao in self.padroes_suspeitos:
            matches = re.finditer(padrao, texto, re.IGNORECASE)
            for match in matches:
                problemas.append({
                    "tipo": "padrao_suspeito",
                    "descricao": descricao,
                    "trecho": match.group(),
                    "posicao": match.start()
                })
                score -= 8

        # 2. Detecção de contradições simples (exemplo básico)
        if "não" in texto.lower() and "sim" in texto.lower():
            # Heurística bem simples (pode melhorar depois)
            pass

        # 3. Frases muito longas e complexas (possível enrolação)
        frases = re.split(r"[.!?]+", texto)
        for frase in frases:
            if len(frase.split()) > 45:
                problemas.append({
                    "tipo": "frase_excessivamente_longa",
                    "descricao": "Frase muito longa pode indicar falta de precisão",
                    "trecho": frase.strip()[:80] + "..."
                })
                score -= 5

        score = max(0, min(100, score))

        # Gera hash do laudo
        laudo_str = f"{texto}{score}{datetime.utcnow().isoformat()}"
        hash_laudo = hashlib.sha256(laudo_str.encode()).hexdigest()

        return {
            "score_confiabilidade": score,
            "total_problemas": len(problemas),
            "problemas": problemas,
            "parecer": self._gerar_parecer(score),
            "hash_laudo": hash_laudo,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

    def _gerar_parecer(self, score: int) -> str:
        if score >= 85:
            return "Alta confiabilidade aparente. Poucos indícios de folga."
        elif score >= 60:
            return "Confiabilidade moderada. Recomenda-se verificação pontual."
        elif score >= 40:
            return "Confiabilidade baixa. Várias possíveis folgas detectadas."
        else:
            return "Confiabilidade muito baixa. Resposta com alto risco de alucinação ou inconsistência."
