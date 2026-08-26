#!/usr/bin/env python3
"""
FSV-Core CLI: Ferramenta de Linha de Comando para Triagem Forense
Integra o banco de referência de autores ao motor de análise geométrica.
"""

import sys
from src.database_mock import SignatureDatabaseMock
from src.analyzer import AdvancedSignatureAnalyzer, comparar_metricas

def executar_auditoria(autor_chave):
    print("==================================================")
    print("     FSV-CORE: AUDITORIA FORENSE DE ASSINATURA    ")
    print("==================================================")
    
    # 1. Carrega o Banco de Dados de Referência
    db = SignatureDatabaseMock()
    registro = db.buscar_referencia(autor_chave)
    
    if registro["status"] == "erro":
        print(f"[ERRO] {registro['mensagem']}")
        print(f"Autores disponíveis no sistema: {db.listar_autores_disponiveis()}")
        return

    print(f"[INFO] Autor Alvo Carregado: {registro['autor']} (Período: {registro['periodo']})")
    metrica_ref = registro["metrica_padrao"]

    # 2. Simula uma matriz de amostra coletada em campo (ex: obra sob análise)
    # 1 = Traço, 0 = Fundo
    amostra_coletada = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,0,0,0,1,0,0],
        [0,0,1,0,0,0,1,1,1,0],
        [0,0,1,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]

    print("[PROCESSANDO] Mapeando geometria de traço da obra sob análise...")
    analisador_teste = AdvancedSignatureAnalyzer(amostra_coletada)
    metrica_teste = analisador_teste.compute_geometric_metrics()

    # 3. Compara as métricas
    score = comparar_metricas(metrica_ref, metrica_teste)

    print("--------------------------------------------------")
    print(f"-> Índice de Compatibilidade Geométrica: {score}%")
    if score >= 90.0:
        print("-> PARECER PRELIMINAR: Alta compatibilidade com o Dataset de Ouro.")
    else:
        print("-> PARECER PRELIMINAR: Divergência estrutural detectada.")
    print("==================================================")

if __name__ == "__main__":
    # Permite escolher o autor via argumento ou usa Portinari como padrão
    alvo = sys.argv[1] if len(sys.argv) > 1 else "portinari_1950"
    executar_auditoria(alvo)
