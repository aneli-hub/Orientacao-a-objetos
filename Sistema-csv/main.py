from controller.cliente_controller import ClienteController

def exibir_menu():
    print("=== Menu ===")
    print("1 - cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Sair do sistema")

def main():
    cliente_controller = ClienteController()

    while True:
        exibir_menu()
        opcao = input("Escolha sua opcao: ")

        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            idade = input("Digite a idade do cliente: ")

            # Salvar no "Banco de dados"
            cliente_controller.criar_cliente(nome, email, idade)

        elif opcao == "2":
            #listar clientes do banco
            clientes = cliente_controller.listar_clientes()

            for index, cliente in enumerate(clientes, 1):
                print(f'{index}, {cliente}')
        
        else:
            print("opção invalida,")
            break
            
if __name__ == "__main__":
    main()