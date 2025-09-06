
class Cliente:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade
        
    # Ao inves de exibir o codigo da memoria, exibe o texto abaixo
    def __repr__(self):
        return f"Cliente(nome={self.nome}, email={self.email}, idade={self.idade})"