#!/usr/bin/env python3
"""
Módulo de Banco de Referência (Database Mock) - FSV-Core
Gerencia o repositório de perfis geométricos de autenticidade para consulta rápida.
"""

class SignatureDatabaseMock:
    """
    Simula um banco de dados local/remoto contendo os padrões
    de referência (padrão 'Gold Standard') de assinaturas históricas.
    """

    def __init__(self):
        # Base simulada com assinaturas de referência cadastradas no sistema
        self.registry = {
            "portinari_1950": {
                "autor": "Candido Portinari",
                "periodo": "1950",
                "metrica_padrao": {
                    "status": "sucesso",
                    "pixels_traco": 15,
                    "centro_massa": [4.5, 2.1],
                    "largura_traco": 9,
                    "altura_traco": 3,
                    "indice_densidade_estrutural": 0.5556
                }
            },
            "picasso_1964": {
                "autor": "Pablo Picasso",
                "periodo": "1964",
                "metrica_padrao": {
                    "status": "sucesso",
                    "pixels_traco": 18,
                    "centro_massa": [5.0, 2.5],
                    "largura_traco": 10,
                    "altura_traco": 4,
                    "indice_densidade_estrutural": 0.6000
                }
            }
        }

    def buscar_referencia(self, chave_autor):
        """
        Busca o perfil de referência de um autor cadastrado no banco.
        """
        if chave_autor in self.registry:
            return self.registry[chave_autor]
        else:
            return {"status": "erro", "mensagem": "Autor/Referência não encontrada no Dataset de Ouro."}

    def listar_autores_disponiveis(self):
        """
        Retorna a lista de referências disponíveis para triagem.
        """
        return list(self.registry.keys())

if __name__ == "__main__":
    print("=== FSV-Core: Teste do Módulo de Banco de Dados ===")
    db = SignatureDatabaseMock()
    print("Autores cadastrados:", db.listar_autores_disponiveis())
    
    ref = db.buscar_referencia("portinari_1950")
    print("Dados de referência recuperados:", ref)
