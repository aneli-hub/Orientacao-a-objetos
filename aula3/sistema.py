from models.Pessoa import Pessoa  


def menu():
    print("1. criar Pessoa")
    print("2. Listar Pessoas")
    print("3. Limpar lista")
    print("9. Sair do sistema")


def iniciarSistema():
    print("Sistema iniciado")
    pessoas = [] # criar lista de pessoas 

    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome: ")
            email = input("Digite o email da pessoa: ")
            pessoa = Pessoa(nome, email) # manifestando a Entidade pessoa
            pessoas.append(pessoa) #adicionando a pessoa na lista
    
        elif opcao == "2":
            for pessoa in pessoas:
                print (pessoa)
                print(f"Nome: {pessoa.get_nome()} - Email: {pessoa.get_email()}")
        

#logica para iniciar automaticamente
if __name__ == "__main__":         
    iniciarSistema()