# DEFINIÇÃO DAS PÁGINAS DO INVENTÁRIO (GUI TABS)
class InventarioProfissional:
    def __init__(self):
        # Criando as abas exclusivas para não dar erro de memória
        self.abas = {
            "DECO_MÓVEIS": [],   # 50.000 Decorações (Carregadas dinamicamente)
            "DECO_BLOCOS": [],   # 1000 Blocos, Slabs e Escadas
            "CONCESSIONARIA": [], # 100 Carros (BMW, Ferrari, etc)
            "ESTRUTURAL": [],    # Portas, Trapdoors e Portões de Garagem
            "BIOMA_NEVE": []     # Itens Futuristas e Capivara
        }

    def organizar_itens(self):
        # Página 1: Decorações Interativas
        for i in range(50000):
            item = f"item_deco_{i}"
            # Otimização: Só carrega o ícone se a página estiver aberta
            self.abas["DECO_MÓVEIS"].append(item)

        # Página 2: Carros de Luxo
        marcas = ["BMW", "Ferrari", "Porsche", "Lambo", "McLaren"]
        for marca in marcas:
            for n in range(20):
                self.abas["CONCESSIONARIA"].append(f"carro_{marca}_{n}")

        # Página 3: Blocos e Estruturas
        for i in range(100):
            self.abas["ESTRUTURAL"].append(f"porta_especial_{i}")
            self.abas["ESTRUTURAL"].append(f"escada_futurista_{i}")

    def renderizar_pagina(self, nome_aba):
        # Isso limpa o "branco" da tela e foca apenas nos itens da aba selecionada
        self.limpar_tela_render()
        for item in self.abas[nome_aba]:
            self.desenhar_icone_com_shader(item)
