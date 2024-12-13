import os
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime


usuarios = {}
eventos = {}
inscricoes = {}


def verificar_senha(senha1, senha2):
    if(senha1 == senha2):
        return True
    else:
        print('        ERRO! SENHAS NÃO COINCIDEM.')
        return False

def validar_email(email):

    if not ("@" in email and ".com" in email):
        print('        POR FAVOR, INFORME UM E-MAIL VÁLIDO!')
        cadastrar_usuario(usuarios)
    else:
        return True

def vericar_evento(titulo, eventos):
    if (titulo in eventos):
        return False
    else:
        return False

def verificar_eventos_exixtentes():
    for evento in eventos:
        if (evento[0] in eventos):
            return False
        else:
            print('        EVENTO JÁ CADASTRADO')
            return False

def validar_login(login, senha, usuarios):

    for chave in usuarios:
        if chave == login and usuarios[chave][2] == senha:
            print(f"        SEJA BEM VINDO, {usuarios[chave][0]}!")
            menu_usuario(usuarios)

def inserir_usuario_arquivo(email, senha, nome, telefone):
    arquivo = open('usuarios.txt','a')
    arquivo.write(f'{email},{senha},{nome},{telefone}\n')
    arquivo.close()

def inserir_participante_arquivo(email, senha, nome, telefone):
    arquivo = open('participantes.txt','a')
    arquivo.write(f'{email},{senha},{nome},{telefone}\n')
    arquivo.close()

def adicionar_usuario(login, usuario, usuarios):
    usuarios[login] = usuario

def adicionar_participante(login, usuario, usuarios, senha, evento):
    usuarios[login, senha] = usuario, evento

def cadastrar_usuario(usuarios):
    print("\n::::::::::::::::::::::... CRIAR CONTA ...::::::::::::::::::::::")
    print("\n::::... Faça seu cadastro e comece a criar seus eventos ...::::")
    nome = input("        NOME: ")
    telefone = input("        TELEFONE: ")
    email = input("        E-MAIL: ")
    validar_email(email)
    senha = input("        SENHA: ")
    senha2 = input("        CONFIRME A SENHA: ")


    login = email
    usuario = [nome, telefone, senha]

    arquivo = open('usuarios.txt', 'a')
    arquivo.close()

    if (verificar_senha(senha, senha2)):

        arquivo = open('usuarios.txt', 'r')
        linhas = arquivo.readlines()
        arquivo.close()

        for linha in linhas:
            mod = linha.replace('\n', '')
            email = mod.split(',')[0]
            if login == email:
                print("        ERRO! E-MAIL JÁ CADASTRADO.")
                return cadastrar_usuario(usuarios)

        adicionar_usuario(login, usuario, usuarios)
        inserir_usuario_arquivo(login, senha, nome, telefone)

        print (usuarios)
        print("        USUÁRIO CADASTRADO COM SUCESSO!")

    else:
        print('        TENTE NOVAMENTE!')
        return cadastrar_usuario(usuarios)

def login_usuario():
    print("\n:::::::::::::... LOGIN ...:::::::::::::")

    login = input("        EMAIL: ")
    senha = input("        SENHA: ")

    login_arquivo()

    for chave in usuarios:
        if chave == login and usuarios[chave][2] == senha:
            print(f"        SEJA BEM VINDO, {usuarios[chave][0]}!")
            menu_usuario(usuarios)
        else:
            print("        ERRO! E-MAIL OU SENHA INCORRETOS.")
            login_usuario()

def menu_principal():
    pass

def login_arquivo():
    print("\n:::::::::::::... LOGIN ...:::::::::::::")

    login = input("        EMAIL: ")
    senha = input("        SENHA: ")

    logado = False

    arquivo = open('usuarios.txt', 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    for linha in linhas:
        mod = linha.replace('\n', '')
        email = mod.split(',')[0]
        senha_usu = mod.split(',')[1]

        if login == email and senha == senha_usu:
            print(f"\n        SEJA BEM VINDO, {mod.split(',')[2]}!")
            menu_usuario(usuarios, login, senha)
            logado = True

        else:
            print("        ERRO! E-MAIL OU SENHA INCORRETOS!")
            menu_principal()

    return logado

def menu_usuario(usuario, login, senha):
    while True:
        print(f"\n:::::::::::::... MENU USUÁRIO ...:::::::::::::\n"
        f"\n        1 - CRIAR NOVO EVENTO"
        f"\n        2 - MEUS EVENTOS"
        f"\n        3 - BUSCAR EVENTO"
        f"\n        4 - REMOVER EVENTO"
        f"\n        5 - PARTICIPAR DE UM EVENTO"
        f"\n        6 - VER VALOR ARRECADADO"      
        f"\n        7 - LISTAR PARTICIPANTES DE UM EVENTO"
        f"\n        8 - CANCELAR INSCRIÇÃO DE UM PARTICIPANTE"
        f"\n        9 - BUSCAR EVENTO POR CRITÉRIOS"
        f"\n        10 - GERAR GRÁFICO DOS PARTICIPANTES DE CADA EVENTO"
        f"\n        0 - SAIR")

        opcao = input("        ESCOLHA UMA OPÇÃO: ")

        if opcao == "1":
            criar_evento(usuario)
        elif opcao == "2":
            listar_eventos(usuario, login, senha)
        elif opcao == "3":
            buscar_evento()
        elif opcao == "4":
            remover_evento(usuario)
        elif opcao == "5":
            participar_evento(usuario, login, senha)
        elif opcao == "6":
            ver_valor_arrecadados()
        elif opcao == "7":
            listar_participantes_evento()
        elif opcao == "8":
            cancelar_inscricao()
        elif opcao == "9":
            buscar_evento_por_criterio()
        elif opcao == "10":
            grafico_participantes()
        elif opcao == "0":
            print("        SAINDO... OBRIGADO POR ACESSAR NOSSO SISTEMA...")
            break
        else:
            print("        OPÇÃO INVÁLIDA.")

def inserir_evento_arquivo(titulo, descricao, data, local, valor, chave):
    arquivo = open('eventos.txt','a')
    arquivo.write(f'{titulo},{descricao},{data},{local},{valor},{chave}\n')
    arquivo.close()

def inserir_inscritos_arquivo(titulo, email):
    arquivo = open('inscritos.txt', 'a')
    arquivo.write(f'{titulo},{email}\n')
    arquivo.close()

def criar_evento(usuarios):
    print("\n:::::::::::::... CRIAR EVENTO ...:::::::::::::")
    titulo = input("        TÍTULO: ")
    descricao = input("        DESCRIÇÃO: ")
    data = input("        DATA DD/MM/AAA: ")
    local = input("        LOCAL: ")
    valor = float(input("        VALOR DA INSCRIÇÃO: "))
    email = input("        INFORME SEU E-MAIL: ")

    #eventos[titulo] = [descricao, data, local, valor, login, []]
    inserir_evento_arquivo(titulo, descricao, data, local, valor, email)
    print("\n        PARABÉNS, SEU EVENTO FOI CRIADO COM SUCESSO!")

def listar_eventos(usuario, login, senha):

    print("\n:::::::::::::... LISTA DE EVENTOS ...:::::::::::::")

    arquivo = open('eventos.txt', 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    email = input("INFORME SEU E-MAIL: ")

    if not linhas:
        print("\n        NENHUM EVENTO ENCONTRADO.")
        return menu_usuario(usuario)

    for linha in linhas:
        mod = linha.replace('\n', '')
        titulo = mod.split(',')[0]
        descricao = mod.split(',')[1]
        data = mod.split(',')[2]
        local = mod.split(',')[3]
        valor = mod.split(',')[4]
        login = mod.split(',')[5]

        if email == login:

            print (f"\nTÍTULO: {titulo}"
                   f"\nDESCRIÇÃO: {descricao}"
                   f"\nDATA: {data}"
                   f"\nLOCAL: {local}"
                   f"\nVALOR R$: {valor}"
                   f"\nCRIADOR: {login}"
                   f"\n-----------------------------")
        else:
            print("VOCÊ NÃO TEM NENHUM EVENTO CRIADO!")
            return menu_usuario(usuarios, login, senha)

def buscar_evento():
    busca = input("\n:::::::::::::... BUSCAR EVENTO ...:::::::::::::"
                  "\n        DIGITE O TÍTULO DO EVENTO: ")

    arquivo = open('eventos.txt', 'a')
    linhas = arquivo.readlines()
    arquivo.close()

    for linha in linhas:
        mod = linha.replace('\n', '')
        encontrado = mod.split(',')[0]
        if busca == encontrado:

            titulo = mod.split(',')[0]
            descricao = mod.split(',')[1]
            data = mod.split(',')[2]
            local = mod.split(',')[3]
            valor = mod.split(',')[4]
            print(f"\n:::::::::::::... EVENTO ENCONTRADO ...:::::::::::::")
            print(f"\n        TÍTULO: {titulo}"
                  f"\n        DESCARIÇÃO: {descricao}"
                  f"\n        DATA: {data}"
                  f"\n        LOCAL: {local}"
                  f"\n        VALOR R$: {valor}"
                  f"\n")
            return menu_usuario(usuarios)

        else:
            print("        NENHUM EVENTO FOI ENCONTRADO.")

def buscar_evento_por_criterio():
    print("\n:::::::::::::... BUSCAR EVENTO POR CRITÉRIOS ...:::::::::::::")
    print("\n        1 - BUSCAR POR DATA")
    print("        2 - BUSCAR POR LOCAL")
    print("        3 - BUSCAR PRO CRIADOR")
    opcao = input("\n        ESCOLHA UMA OPÇÃO: ")

    criterio = ""
    if opcao == "1":
        criterio = input("\n        DIGITE A DATA (DD/MM/AAAA): ")
        campo = 2
    elif opcao == "2":
        criterio = input("\n        DIGITE O LOCAL: ")
        campo = 3
    elif opcao == "3":
        criterio = input("\n        DIGITE O E-MAIL DO CRIADOR: ")
        campo = 5
    else:
        print("\n        OPÇÃO INVÁLIDA!")
        return


    arquivo = open('eventos.txt', 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    eventos_encontrados = [
        linha for linha in linhas if linha.split(',')[campo] == criterio
    ]

    if eventos_encontrados:
        print("\nEVENTOS ENCONTRADOS:")
        for evento in eventos_encontrados:
            detalhes = evento.strip().split(',')
            print(f"\n        TÍTULO: {detalhes[0]}"
                  f"\n        DESCRIÇÃO: {detalhes[1]}"
                  f"\n        DATA: {detalhes[2]}"
                  f"\n        LOCAL: {detalhes[3]}"
                  f"\n        VALOR: R$ {detalhes[4]}"
                  f"\n        CRIADOR: {detalhes[5]}"
                  f"\n-----------------------------")
    else:
        print("\nNENHUM EVENTO ENCONTRADO COM ESSE CRITÉRIO")

def remover_evento(usuario):
    titulo = input("\n:::::::::::::... REMOVER EVENTO ...:::::::::::::"
                   "\n        DIGITE O TÍTULO DO EVENTO: ")


    arquivo = open('eventos.txt', 'a')
    linhas = arquivo.readlines()
    arquivo.close()

    eventos_restantes = []
    evento_encontrado = False

    for linha in linhas:
        mod = linha.replace('\n', '')
        encontrado = mod.split(',')[0]
        if titulo == encontrado:
            evento_encontrado = True
        else:
            eventos_restantes.append(linha)

        with open('eventos.txt', 'a') as arquivo:
            arquivo.writelines(eventos_restantes)

        print(f"EVENTO {titulo} REMOVIDO COM SUCESSO!")

    if not evento_encontrado:
        print(f"        ERRO! EVENTO NÃO ENCONTRADO"
              f"\n        VERIFIQUE SE VOCÊ TEM PERMISSÃO PARA REMOVER EVENTOS!")
        return menu_usuario(usuarios)

def participar_evento(usuario, login, senha):

    print("\n:::::::::::::... INSCRIÇÃO EVENTO ...:::::::::::::")
    print("\n:::::::::::::... LISTA DE EVENTOS ...:::::::::::::")

    arquivo = open('eventos.txt', 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    if not linhas:
        print("\n        NENHUM EVENTO DISPONÍVEL PARA INSCRIÇÃO.")
        return menu_usuario(usuario, login, senha)

    for linha in linhas:
        mod = linha.replace('\n', '')
        titulo = mod.split(',')[0]
        descricao = mod.split(',')[1]
        data = mod.split(',')[2]
        local = mod.split(',')[3]
        valor = mod.split(',')[4]

        print(f"\nTítulo: {titulo}"
              f"\nDescrição: {descricao}"
              f"\nData: {data}     |     Local: {local}"
              f"\nValor R$: {valor}"
              f"\n-----------------------------")



    arquivo = open('eventos.txt', 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    titulo =input("\nINFORME QUAL EVENTO VOCÊ DESEJA SE INSCREVER: ")

    for linha in linhas:

        mod = linha.replace('\n', '')
        encontrado = mod.split(',')[0]
        if titulo == encontrado:

            arquivo = open('usuarios.txt', 'r')
            linhas = arquivo.readlines()
            arquivo.close()

            email = input("INFORME SEU E-MAIL: ")

            for linha in linhas:
                mod = linha.replace('\n', '')
                usu = mod.split(',')[0]
                if email == usu:

                    arquivo = open('inscritos.txt', 'r')
                    linhas = arquivo.readlines()
                    arquivo.close()

                    if len(linhas) == 0:
                        inscricoes[titulo] = [email]
                        inserir_inscritos_arquivo(titulo, email)

                    else:
                        for linha in linhas:
                                mod = linha.replace('\n', '')
                                achei = mod.split(',')[1]

                                if email == achei:
                                    print("        USUÁRIO JÁ CADASTRADO!")
                                    menu_usuario(usuarios, login, senha)

                                else:
                                    print("\n        INSCRIÇÃO REALIZADA COM SUCESSO")
                                    inscricoes[titulo] = [email]
                                    inserir_inscritos_arquivo(titulo, email)

def ver_valor_arrecadados():

    arquivo = open('eventos.txt', 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    busca = input("\nINFORME QUAL EVENTO VOCÊ DESEJA CONSULTAR VALORES: ")

    total_valor = 0
    eventos_participantes = {}
    participantes = 0

    for linha in linhas:
        mod = linha.strip().split(',')
        titulo = mod[0]
        valor = float(mod[4])
        participantes = mod[5]

        if titulo == busca:

            validacao = input("\nINFORME SEI E-MAIL PARA VALIDAÇÃO: ")

            arquivo = open('eventos.txt', 'r')
            linhas = arquivo.readlines()
            arquivo.close()

            for linha in linhas:
                mod = linha.strip().split(',')
                titulo = mod[0]
                criador = mod[5]

                if criador == validacao:

                    arquivo = open('inscritos.txt', 'r')
                    linhas = arquivo.readlines()
                    arquivo.close()

                    for linha in linhas:
                        mod = linha.replace('\n', '')
                        titulo_inscrito = mod.split(',')[0]
                        if titulo == titulo_inscrito:
                            total_valor += valor * len(linhas)
                            eventos_participantes[titulo] = len(linhas)

                    print("\n:::::::::::::... RELATÓRIO DE EVENTOS ...:::::::::::::")
                    for evento, qtd in eventos_participantes.items():
                        print(f"\nEVENTO: {evento}"
                              f"\nPARTICIPANTES: {qtd}")
                    print(f"\nVALOR TOTAL ARRECADADO: R$ {total_valor:.2f}")

                else:
                    print("\n        VOCÊ NÃO TEM PERMISSÃO PARA CONSULTAR VALORES")

def listar_participantes_evento():
    print("\n:::::::::::::... LISTAR PARTICIPANTES DE UM EVENTO ...:::::::::::::")

    arquivo = open('eventos.txt', 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    busca = input("        DIGITE O TÍTULO DO EVENTO: ")

    for linha in linhas:
        mod = linha.strip().split(',')
        titulo = mod[0]

        if titulo == busca:

            validacao = input("\nINFORME SEI E-MAIL PARA VALIDAÇÃO: ")

            arquivo = open('eventos.txt', 'r')
            linhas = arquivo.readlines()
            arquivo.close()

            for linha in linhas:
                mod = linha.strip().split(',')
                titulo = mod[0]
                criador = mod[5]

                if criador == validacao:

                    arquivo = open('inscritos.txt', 'r')
                    linhas = arquivo.readlines()
                    arquivo.close()

                    if not linhas:
                        print("\n        NENHUM PARTICIPANTE ENCONTRADO PARA QUALQUER EVENTO.")
                        return menu_usuario()

                    participantes = [linha.split(',')[1].strip() for linha in linhas if linha.split(',')[0] == titulo]

                    if participantes:
                        print(f"\n        PARTICIPANTES DO EVENTO '{titulo}':")
                        for i, participante in enumerate(participantes, 1):
                            print(f"        {i}. {participante}")
                    else:
                        print("\n        NENHUM PARTICIPANTE ENCONTRADO PARA ESTE EVENTO.")

                else:
                    print("\n        VOCÊ NÃO TEM PERMISSÃO PARA ACESSAR OS PARTICIPANTES DESSE EVENTO")

def grafico_participantes():

    arquivo = open('inscritos.txt', 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    eventos_participantes = {}

    for linha in linhas:
        mod = linha.strip().split(',')
        evento = mod[0]
        if evento in eventos_participantes:
            eventos_participantes[evento] += 1
        else:
            eventos_participantes[evento] = 1

    eventos = list(eventos_participantes.keys())
    participantes = list(eventos_participantes.values())

    plt.figure(figsize=(10, 6))
    plt.bar(eventos, participantes, color='skyblue')
    plt.title('QUANTIDADE DE PARTICIPANTES POR EVENTO', fontsize=16)
    plt.xlabel('EVENTOS', fontsize=14)
    plt.ylabel('NÚMERO DE PARTICIPANTES', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.savefig('graficoparticipantes.png')
    plt.show()

def cancelar_inscricao():
    print("\n:::::::::::::... CANCELAR INSCRIÇÃO DE UM PARTICIPANTE ...:::::::::::::")

    titulo = input("        DIGITE O TÍTULO DO EVENTO: ")
    email_criador = input("        DIGITE SEU E-MAIL (CRIADOR DO EVENTO): ")

    arquivo = open('eventos.txt', 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    evento_encontrado = False

    for linha in linhas:
        dados = linha.strip().split(',')
        if dados[0] == titulo and dados[5] == email_criador:
            evento_encontrado = True
            break

    if not evento_encontrado:
        print("\n        ERRO! EVENTO NÃO ENCONTRADO OU VOCÊ NÃO É O CRIADOR.")
        return menu_usuario()

    with open('inscritos.txt', 'r') as arquivo_inscritos:
        linhas_inscritos = arquivo_inscritos.readlines()

    participantes = [linha.strip().split(',')[1] for linha in linhas_inscritos if linha.strip().split(',')[0] == titulo]

    if not participantes:
        print("\n        NÃO HÁ INSCRITOS NESTE EVENTO.")
        return

    print("\n        PARTICIPANTES INSCRITOS:")
    for usu, participante in enumerate(participantes, 1):
        print(f"        {usu}. {participante}")

    email_participante = input("\n        DIGITE O E-MAIL DO PARTICIPANTE A SER REMOVIDO: ")

    if email_participante not in participantes:
        print("\n        ERRO! PARTICIPANTE NÃO ENCONTRADO NO EVENTO.")
        return

    with open('inscritos.txt', 'w') as arquivo_inscritos:
        for linha in linhas_inscritos:
            dados = linha.strip().split(',')
            if not (dados[0] == titulo and dados[1] == email_participante):
                arquivo_inscritos.write(linha)

    print(f"\n        PARTICIPANTE {email_participante} REMOVIDO DO EVENTO '{titulo}' COM SUCESSO!")

def area_participante(usuarios):
    while True:
        print("\n:::::::::::::... ÁREA DO PARTICIPANTE ...:::::::::::::")
        print(f"\n        1 - CERTIFICADO"
              f"\n        2 - MINHAS INSCRIÇÕES"
              f"\n        0 - SAIR")

        opcao = input("        ESCOLHA UMA OPÇÃO: ")

        if opcao == "1":
            gerar_certificado()
        elif opcao == "2":
            listar_minhas_inscricoes()
        elif opcao == "0":
            print("        SAINDO DA ÁREA DO PARTICIPANTE...")
            break
        else:
            print("        OPÇÃO INVÁLIDA.")

def listar_minhas_inscricoes():
    print("\n:::::::::::::... MINHAS INSCRIÇÕES ...:::::::::::::")

    email_participante = input("        DIGITE SEU E-MAIL: ")

    with open('inscritos.txt', 'r') as arquivo:
        inscricoes = arquivo.readlines()

    eventos_inscritos = [linha.strip().split(',')[0] for linha in inscricoes if linha.strip().split(',')[1] == email_participante]

    if eventos_inscritos:
        print(f"\n        EVENTOS QUE VOCÊ ESTÁ INSCRITO:")
        for evento in eventos_inscritos:
            print(f"        - {evento}")
    else:
        print("\n        VOCÊ NÃO ESTÁ INSCRITO EM NENHUM EVENTO.")

def gerar_certificado():
    print("\n:::::::::::::... GERANDO CERTIFICADO ...:::::::::::::")

    email_participante = input("        DIGITE SEU E-MAIL PARA GERAR O CERTIFICADO: ")

    with open('inscritos.txt', 'r') as arquivo:
        inscritos = arquivo.readlines()

    eventos_participante = [linha.strip().split(',')[0] for linha in inscritos if
                            linha.strip().split(',')[1] == email_participante]

    if eventos_participante:
        print(f"\n        VOCÊ ESTÁ INSCRITO NOS SEGUINTES EVENTOS:")
        for evento in eventos_participante:
            print(f"        - {evento}")

        evento_escolhido = input("\n        DIGITE O NOME DO EVENTO PARA GERAR O CERTIFICADO: ")

        if evento_escolhido in eventos_participante:

            certificado_pdf(evento_escolhido, email_participante)
        else:
            print("        ERRO! VOCÊ NÃO ESTÁ INSCRITO NESTE EVENTO.")
    else:
        print("        ERRO! VOCÊ NÃO ESTÁ INSCRITO EM NENHUM EVENTO.")

def certificado_pdf(evento, email_participante):

    nome_arquivo = f"{evento}_certificado_{email_participante}.pdf"
    caminho_documentos = os.path.expanduser('~/Documents')  # Diretório de documentos do usuário
    caminho_arquivo = os.path.join(caminho_documentos, nome_arquivo)

    c = canvas.Canvas(caminho_arquivo, pagesize=letter)

    c.setFont("Helvetica-Bold", 24)
    c.drawString(200, 750, f"CERTIFICADO DE PARTICIPAÇÃO")

    c.setFont("Helvetica", 18)
    c.drawString(100, 700, f"Este certificado é concedido a:")

    c.setFont("Helvetica-Bold", 22)
    c.drawString(100, 650, f"{email_participante}")

    c.setFont("Helvetica", 18)
    c.drawString(100, 600, f"Como participante do evento:")
    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, 550, f"{evento}")

    c.setFont("Helvetica", 12)
    c.drawString(100, 500, f"Data de emissão: {datetime.now().strftime('%d/%m/%Y')}")

    c.showPage()
    c.save()

    print(f"\n        CERTIFICADO GERADO COM SUCESSO!")
    print(f"        O CERTIFICADO FOI SALVO EM: {caminho_arquivo}")