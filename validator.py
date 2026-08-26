#!/usr/bin/env python3
"""
Módulo de Validação e Sanitização (Validator Core) - FSV-Core
Garante que dados corrompidos ou inválidos nunca cheguem ao motor matemático.
"""

class DataSanitizer:
    """
    Filtro determinístico de integridade para matrizes de traço e metadados.
    """
    
    @staticmethod
    def validar_matriz_assinatura(matriz):
        """
        Verifica se a matriz de pixels enviada para análise é estruturalmente válida.
        Elimina falhas antes que o motor matemático processe dados incorretos.
        """
        if not isinstance(matriz, list) or len(matriz) == 0:
            return {"valido": False, "erro": "A matriz de entrada é nula ou não é uma lista válida."}
        
        # Verifica se todas as linhas têm o mesmo comprimento (consistência geométrica)
        primeira_linha_tam = len(matriz[0])
        for i, linha in enumerate(matriz):
            if not isinstance(linha, list):
                return {"valido": False, "erro": f"A linha {i} da matriz não é uma lista válida."}
            if len(linha) != primeira_linha_tam:
                return {"valido": False, "erro": "Inconsistência dimensional: linhas com comprimentos diferentes."}
            
            # Valida se os elementos são estritamente binários (0 ou 1)
            for val in linha:
                if val not in (0, 1):
                    return {"valido": False, "erro": f"Valor não permitido encontrado na matriz: '{val}'. Use apenas 0 ou 1."}
                    
        return {"valido": True, "erro": None}

if __name__ == "__main__":
    print("=== FSV-Core: Teste do Módulo de Validação ===")
    
    # Matriz válida de teste
    matriz_boa = [[0, 1], [1, 0]]
    res = DataSanitizer.validar_matriz_assinatura(matriz_boa)
    print("Teste com dados válidos:", res)

    # Matriz corrompida de teste
    matriz_ruim = [[0, 1], [2, 5]] # Valores incorretos
    res_ruim = DataSanitizer.validar_matriz_assinatura(matriz_ruim)
    print("Teste com dados corrompidos:", res_ruim)
