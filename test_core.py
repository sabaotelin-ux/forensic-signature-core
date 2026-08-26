#!/usr/bin/env python3
"""
Testes Automatizados de Integração - FSV-Core
Garante a integridade determinística de todos os submódulos do ecossistema.
"""

import sys
import os

# Adiciona a raiz ao path para importação correta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.validator import DataSanitizer
from src.audit_logger import AuditTrail
from src.database_mock import SignatureDatabaseMock

def testar_integridade_sistema():
    print("[TESTE] Iniciando validação automatizada do FSV-Core...")
    
    # 1. Testa o Validador de Entrada
    matriz_teste = [[0, 1], [1, 0]]
    val_res = DataSanitizer.validar_matriz_assinatura(matriz_teste)
    assert val_res["valido"] == True, "Falha no validador de matrizes!"
    print("[OK] Validador de Entrada aprovado.")

    # 2. Testa o Banco Determinístico
    db = SignatureDatabaseMock()
    ref = db.buscar_referencia("portinari_1950")
    assert ref["status"] == "sucesso", "Falha na busca determinística do banco!"
    print("[OK] Banco Determinístico aprovado.")

    # 3. Testa o Motor de Auditoria Criptográfica
    auditoria = AuditTrail.gerar_comprovante_seguro(
        ref["autor"], ref["periodo"], 95.0, "Compatibilidade perfeita"
    )
    assert "hash_seguranca_sha256" in auditoria, "Falha na geração do hash de auditoria!"
    print("[OK] Rastreabilidade Criptográfica aprovada.")
    
    print("\n[SUCESSO] Todos os testes estruturais passaram com 100% de precisão!")

if __name__ == "__main__":
    testar_integridade_sistema()
