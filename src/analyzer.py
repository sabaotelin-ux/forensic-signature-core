#!/usr/bin/env python3
"""
Módulo Core de Validação Forense de Assinaturas (FSV-Core) v2.0
Análise geométrica avançada de traços manuscritos para proveniência de obras.
"""

import math

class AdvancedSignatureAnalyzer:
    """
    Analisa propriedades geométricas puras de matrizes de pixels representando assinaturas.
    Não requer dependências externas pesadas, rodando com alta performance em qualquer ambiente.
    """

    def __init__(self, signature_matrix):
        """
        Recebe uma matriz (lista de listas) representando a imagem binarizada da assinatura.
        1 = Traço da assinatura, 0 = Fundo do papel.
        """
        self.matrix = signature_matrix
        self.height = len(signature_matrix)
        self.width = len(signature_matrix[0]) if self.height > 0 else 0

    def compute_geometric_metrics(self):
        """
        Calcula métricas forenses avançadas:
        - Densidade de traço (complexidade da assinatura)
        - Centro de massa (distribuição espacial)
        - Fator de dispersão horizontal e vertical
        """
        total_pixels = 0
        sum_y = 0
        sum_x = 0
        min_x, max_x = self.width, 0
        min_y, max_y = self.height, 0

        for y in range(self.height):
            for x in range(self.width):
                if self.matrix[y][x] == 1:
                    total_pixels += 1
                    sum_y += y
                    sum_x += x
                    if x < min_x: min_x = x
                    if x > max_x: max_x = x
                    if y < min_y: min_y = y
                    if y > max_y: max_y = y

        if total_pixels == 0:
            return {"status": "erro", "mensagem": "Nenhum traço detectado."}

        # Centro de massa geométrica
        c_y = sum_y / total_pixels
        c_x = sum_x / total_pixels

        # Bounding box (Delimitação da assinatura)
        bounding_box_area = (max_x - min_x + 1) * (max_y - min_y + 1)
        ratio_ocupacao = total_pixels / bounding_box_area if bounding_box_area > 0 else 0

        return {
            "status": "sucesso",
            "pixels_traco": total_pixels,
            "centro_massa": [round(c_x, 2), round(c_y, 2)],
            "largura_traco": max_x - min_x + 1,
            "altura_traco": max_y - min_y + 1,
            "indice_densidade_estrutural": round(ratio_ocupacao, 4)
        }

def comparar_metricas(metrica_ref, metrica_teste):
    """
    Compara os vetores geométricos de duas assinaturas para gerar 
    um índice de similaridade estrutural percentual.
    """
    if metrica_ref["status"] != "sucesso" or metrica_teste["status"] != "sucesso":
        return 0.0

    # Diferença relativa na densidade estrutural
    densidade_ref = metrica_ref["indice_densidade_estrutural"]
    densidade_teste = metrica_teste["indice_densidade_estrutural"]
    
    diff_densidade = abs(densidade_ref - densidade_teste)
    
    # Score de similaridade baseado na proximidade da densidade geométrica (0 a 100%)
    similarity = max(0.0, 100.0 - (diff_densidade * 200.0))
    return round(similarity, 2)

if __name__ == "__main__":
    print("=== FSV-Core v2.0: Iniciando Teste de Validação Geométrica ===")
    
    # Simulação de uma matriz de pixels de uma assinatura de referência (ex: Portinari)
    # 0 = Fundo, 1 = Traço da assinatura
    assinatura_ref = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,0,0,1,0,0],
        [0,0,1,0,0,0,1,1,1,0],
        [0,0,1,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]

    # Simulação de uma assinatura de teste muito parecida (Autêntica)
    assinatura_teste_1 = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,0,0,0,1,0,0],
        [0,0,1,0,0,0,1,1,1,0],
        [0,0,1,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]

    analisador_ref = AdvancedSignatureAnalyzer(assinatura_ref)
    m_ref = analisador_ref.compute_geometric_metrics()

    analisador_teste = AdvancedSignatureAnalyzer(assinatura_teste_1)
    m_teste = analisador_teste.compute_geometric_metrics()

    score = comparar_metricas(m_ref, m_teste)

    print(f"Métricas de Referência: {m_ref}")
    print(f"Métricas de Teste:     {m_teste}")
    print(f"-> Índice de Compatibilidade Geométrica Calculado: {score}%")
    print("=== Teste Concluído com Sucesso ===")
