import json # lidar com arquivos json
from pathlib import Path # lidar com caminhos de windwos

# json -> javascript object notation

class Bancofake:
    def __init__(self, arquivo_db="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes": []} # clientes iniciando como vazio

        # carregar valores anteriores salvos 
        self.carregar()

    def carregar(self):
        """
        Carregar os dados do arquivo json, se existir.
        caspo contrário, inicie banco novo.
        """

        caminho = Path(self.arquivo_db)
        #verifique se arquivo existe
        if caminho.is_file():
            # abrindo arquivo no modo leitura com utf-8 (pt-br)
            with open(caminho, "r", encoding="utf-8") as arquivo:
                #carregar dados anteriores ja salvos
                self.dados = json.load(arquivo)
        else:
            #chamar funcao para criar novo arquivo
            self.salvar()

    def salvar(self):
        """
        Salvar o conteudo do self.dados no arquivo json
        """
        #abrir arquivo no modo escrita com utf-8 (pt-br)
        with open(self.arquivo_db, "w", encoding="utf-8") as dados:
            #realizar um Dump de python para json
            # ensure_ascii=False -> para aceitar caracteres, emogis, etc
            # indent=4 -> identação de 4 espaços
            json.dump(self.dados, dados, ensure_ascii=False, indent=4)  
    
    def adicionar_cliente(self, cliente_dict):
        self.dados["clientes"].append(cliente_dict)
        self.salvar()  
    
    def listar_clientes(self):
        return self.dados["clientes"]