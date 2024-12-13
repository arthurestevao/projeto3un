from funcoes_evento import *

opcao = -1

while (opcao != 0):
    print("\n::::::::::::::::::... TYPE EVENTS ...::::::::::::::::::")
    print(f"\n        1 - CRIAR MINHA CONTA"
        f"\n        2 - LOGIN"
        f"\n        3 - ÁREA DO PARTICIPANTE"
          f"\n        4 - BUSCAR EVENTOS"
          f"\n        0 - SAIR")

    opcao = input("        ESCOLHA UMA OPÇÃO: ")

    if opcao == "1":
        cadastrar_usuario(usuarios)
    elif opcao == "2":
        login_arquivo()
    elif opcao == "3":
        area_participante(usuarios)
    elif opcao == "0":
        print("        SAINDO... OBRIGADO POR ACESSAR NOSSO SISTEMA...")
        break
    else:
        print("        DIGITE UMA OPÇÃO VÁLIDA.")