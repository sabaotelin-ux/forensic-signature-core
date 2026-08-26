#!/usr/bin/env python3
"""
Motor Híbrido de Busca Determinística (Hybrid Search Core)
Resolve o problema de alucinação de IAs fazendo buscas exatas e por 
palavras-chave em bases locais antes de qualquer resposta.
"""

class HybridSearchEngine:
    def __init__(self, base_dados):
        # Base de dados estruturada local (substitui a memória incerta da IA)
        self.database = base_dados

    def busca_exata_por_termo(self, campo, valor):
        """
        Retorna registros que correspondem exatamente ao critério buscado.
        Zero probabilidade, zero alucinação: 100% determinístico.
        """
        resultados = []
        for item_id, dados in self.database.items():
            if dados.get(campo) == valor:
                resultados.append({"id": item_id, **dados})
        return resultados

    def busca_por_palavra_chave(self, termo_chave):
        """
        Varre os campos de texto buscando ocorrências parciais de forma estruturada.
        """
        termo_chave = termo_chave.lower()
        resultados = []
        for item_id, dados in self.database.items]:
            texto_total = " ".join([str(v) for v in dados.values()]).lower()
            if termo_chave in texto_total:
                resultados.append({"id": item_id, **dados})
        return resultados

if __name__ == "__main__":
    # Exemplo prático aplicado ao seu nicho (Acervo / Obras Raras)
    acervo_local = {
        "livro_01": {"titulo": "Obra Rara Portinari", "ano": 1950, "autor": "Candido Portinari", "local": "Gaveta A"},
        "livro_02": {"titulo": "Edicao Historica Picasso", "ano": 1964, "autor": "Pablo Picasso", "local": "Gaveta B"},
    }

    motor = HybridSearchEngine(acervo_local)
    
    print("--- Teste de Busca Exata por Autor ---")
    res_exata = motor.busca_exata_por_termo("autor", "Candido Portinari")
    print(res_exata)

    print("\n--- Teste de Busca por Palavra-Chave (Termo: '1964') ---")
    res_kw = motor.busca_por_palavra_chave("1964")
    print(res_kw)
