import os

restaurantes = [
    {"Nome": "Praça", "Categoria": "Japonesa", "Ativo": False},
    {"Nome": "Pizza Suprema", "Categoria": "Japonesa", "Ativo": True},
    {"Nome": "Cantina", "Categoria": "Italiano", "Ativo": False},
]


def exibir_nome_programa():
    print(
        """
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
"""
    )


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar status restaurante")
    print("4. Sair\n")


def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu do programa!")
    main()


def opcao_invalida():
    print("Opção inválida")
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    os.system("clear")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    exibir_subtitulo("cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(
        f"Digite o nome da categoria do restaurante {nome_do_restaurante}: "
    )
    dados_do_restaurante = {
        "Nome": nome_do_restaurante,
        "Categoria": categoria,
        "Ativo": False,
    }
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo("alterando STATUS do restaurante")
    nome_restaurante = input(
        "Digite o nome do restaurante que deseja alterar o STATUS: "
    )
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["Nome"]:
            restaurante_encontrado = True
            restaurante["Ativo"] = not restaurante["Ativo"]
            mensagem = (
                f"O restaurante {nome_restaurante} foi ativado com sucesso"
                if restaurante["Ativo"]
                else f"O restaurante {nome_restaurante} desativado com sucesso"
            )
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes")
    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["Nome"]
        categoria = restaurante["Categoria"]
        ativo = "Ativado" if restaurante["Ativo"] else "Desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    voltar_ao_menu_principal()


def finalizar_app():
    exibir_subtitulo("finalizando o app")


def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system("clear")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()
