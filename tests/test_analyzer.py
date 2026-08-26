#!/usr/bin/env python3
"""
Módulo de Testes Unitários - FSV-Core
Valida a precisão matemática do motor de densidade e similaridade geométrica.
"""

import unittest
from src.analyzer import AdvancedSignatureAnalyzer, comparar_metricas

class TestSignatureGeometricEngine(unittest.TestCase):

    def setUp(self):
        # Matriz padrão de referência válida
        self.ref_matrix = [
            [0,0,0,0,0],
            [0,1,1,1,0],
            [0,0,1,0,0],
            [0,0,0,0,0]
        ]
        self.analyzer_ref = AdvancedSignatureAnalyzer(self.ref_matrix)

    def test_computacao_metricas_sucesso(self):
        metrics = self.analyzer_ref.compute_geometric_metrics()
        self.assertEqual(metrics["status"], "sucesso")
        self.assertGreater(metrics["pixels_traco"], 0)
        self.assertIn("centro_massa", metrics)

def test_comparacao_similaridade_alta(self):
        # Matriz muito similar
        teste_matrix = [
            [0,0,0,0,0],
            [0,1,1,0,0],
            [0,0,1,1,0],
            [0,0,0,0,0]
        ]
        analyzer_teste = AdvancedSignatureAnalyzer(teste_matrix)
        m_ref = self.analyzer_ref.compute_geometric_metrics()
        m_teste = analyzer_teste.compute_geometric_metrics()
        
        score = comparar_metricas(m_ref, m_teste)
        self.assertGreaterEqual(score, 50.0)

if __name__ == "__main__":
    unittest.main()
