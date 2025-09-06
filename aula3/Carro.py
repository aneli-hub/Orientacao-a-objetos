
class Carro:

    #configuração inicial do objeto
    def __init__(self, nome, cor, modelo, ano , marca):
        #atributos #self (eu)
        self.nome = nome
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
             #métodos
    def correr(self):
        print(f"O carro {self.nome} está correndo")

    def parar(self):
        print(f"O carro {self.nome} pastilha está ruim")

    def ligar(self):
        print(f"O carro {self.nome} está ligado")


passatiCarro = Carro("Passat", "Prata", "Sedan", 2020, "Volkswagen")
passatiCarro.ligar()

passatiCarro.correr()
passatiCarro.parar()