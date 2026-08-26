[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENÇA)

# 🔍 FSV-Core: Motor de Assinaturas e Proveniências Forenses (v2.0)

> **FSV-Core** é um motor computacional de código aberto projetado para a análise geométrica, mapeamento matricial e rastreamento forense de assinaturas, rubricas e dedicatórias em livros raros, gravuras e manuscritos históricos.

---

## 💡 O Problema
Autenticar obras raras e assinaturas históricas manualmente é um processo lento, sujeito a falhas humanas e caro. Além disso, IAs tradicionais baseadas apenas em texto frequentemente sofrem com **alucinações**.

## 🚀 A Solução (Abordagem Híbrida)
O **FSV-Core** resolve isso combinando:
1. **Precisão Matemática Determinística:** Análise geométrica de traços por matrizes e distâncias euclidianas.
2. **Busca Híbrida Blindada:** Cruzamento estrito com um banco de dados de referência validado.
3. **Trilha de Auditoria Criptográfica:** Geração de laudos com assinaturas SHA-256 inalteráveis.

---

## 📂 Arquitetura do Repositório

| Módulo / Arquivo | Função Principal |
| :--- | :--- |
| **`src/analyzer.py`** | Núcleo de cálculo geométrico e métricas de traço. |
| **`src/validator.py`** | Sanitização estrita e bloqueio de dados corrompidos. |
| **`src/hybrid_search.py`** | Sistema de busca combinada (texto + matriz). |
| **`src/database_mock.py`** | Base de acervo histórico de referência isolada. |
| **`src/audit_logger.py`** | Geração de hashes SHA-256 para laudos periciais. |
| **`src/vision_extractor.py`** | Visão computacional para conversão de fotos em matrizes. |
| **`src/feedback_memory.py`** | Memória dinâmica para aprendizado por casos. |
| **`src/api.py`** | Gateway FastAPI de alta performance. |
| **`executar.py`** | Orquestrador para inicialização segura do servidor. |
| **`index.html`** | Painel visual web intuitivo para triagem. |
| **`testes/test_core.py`**| Bateria de testes automatizados de integridade. |

---

## 🛠️ Como Executar e Testar Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/sabaotelin-ux/forensic-signature-core.git](https://github.com/sabaotelin-ux/forensic-signature-core.git)
   cd forensic-signature-core

