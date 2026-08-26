![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
 #FSV-Core: Forensic Signature & Provenance Engine (v2.0)

**FSV-Core** é um motor computacional open-source projetado para a análise geométrica, mapeamento matricial e triagem forense de assinaturas, rubricas e dedicatórias em livros raros, gravuras e manuscritos históricos.

## 💡 O Problema
O mercado global de arte, antiguidades e acervos literários raros movimenta bilhões, mas sofre constantemente com fraudes, cópias grosseiras e a escassez de peritos caligráficos disponíveis para vistorias preliminares imediatas em obras recém-descobertas.

## 🚀 A Solução (Abordagem v2.0)
Diferente de ferramentas tradicionais de OCR focadas em texto comercial, o **FSV-Core v2.0** implementa um motor de processamento matemático de traços baseado em:
1. **Mapeamento Matricial de Pixels:** Conversão do suporte gráfico em matrizes de coordenadas discretas, isolando o traço do fundo físico.
2. **Análise de Densidade Estrutural:** Cálculo de proporção de ocupação, bounding box dinâmica e centro de massa geométrica.
3. **Índice de Compatibilidade Percentual:** Algoritmo matemático para mensurar a similaridade estrutural entre uma assinatura de referência e uma amostra de teste.

## 🛠️ Arquitetura do Repositório
* `src/analyzer.py` — Motor matemático principal de processamento de matrizes e métricas forenses.
* `data/` — Diretório reservado para conjuntos de referência (Datasets de Ouro).

## 📊 Exemplo de Uso Técnico (v2.0)
O motor processa matrizes de pixels representando o traço da escrita para gerar relatórios de compatibilidade geométrica de forma leve, sem dependências externas complexas:

```python
from src.analyzer import AdvancedSignatureAnalyzer, comparar_metricas

# Matrizes simuladas de binarização de traço (1 = Traço, 0 = Fundo)
# ...

