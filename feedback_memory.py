#!/usr/bin/env python3
"""
Módulo de Memória Dinâmica e Feedback (Feedback Memory Core) - FSV-Core
Permite que o sistema registre novas amostras validadas por peritos sem alterar o código.
"""

import json
import os

class DynamicKnowledgeBase:
    """
    Gerencia a expansão determinística do acervo com base em validações reais.
    """
    def __init__(self, filepath="src/dynamic_db.json"):
        self.filepath = filepath
        self._inicializar_base()

    def _inicializar_base(self):
        if not os.path.exists(self.filepath):
            dados_iniciais = {
                "portinari_1950": {"autor": "Candido Portinari", "periodo": "1950", "amostras_coletadas": 1}
            }
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(dados_iniciais, f, indent=4, ensure_ascii=False)

    def registrar_nova_amostra_validada(self, chave_autor, novos_dados):
        """
        Adiciona uma nova assinatura validada ao acervo de forma persistente.
        """
        with open(self.filepath, "r", encoding="utf-8") as f:
            base = json.load(f)
            
        if chave_autor in base:
            base[chave_autor]["amostras_coletadas"] += 1
        else:
            base[chave_autor] = {"autor": novos_dados.get("autor"), "periodo": novos_dados.get("periodo"), "amostras_coletadas": 1}
            
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(base, f, indent=4, ensure_ascii=False)
            
        return {"status": "sucesso", "mensagem": "Base de conhecimento atualizada com sucesso."}

if __name__ == "__main__":
    db_dinamico = DynamicKnowledgeBase()
    res = db_dinamico.registrar_nova_amostra_validada("portinari_1950", {"autor": "Candido Portinari", "periodo": "1950"})
    print("Teste de Memória Dinâmica:", res)
