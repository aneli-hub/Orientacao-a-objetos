from models.cliente import Cliente
from database.database import Bancofake

class ClienteController:
    def __init__(self):
        # conexao com o banco de dados
        self.database = Bancofake()

    def criar_cliente(self, nome, email, idade):
        #Criar objeto cliente
        novo_cliente = Cliente(nome, email, idade)

        # convertendo para dict -> Json
        dict_cliente = {
            "nome": novo_cliente.nome,
            "email": novo_cliente.email,
            "idade": novo_cliente.idade
        }

        self.database.adicionar_cliente(dict_cliente)
        print("Cliente adicionado com sucesso!")

    def listar_clientes(self):
        """
        Retornar uma lista com todos os clientes
        """
        return self.database.listar_clientes()