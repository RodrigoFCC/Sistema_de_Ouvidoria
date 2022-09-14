import ocorre

i = 1
print('-=' * 20)
print(f'{"BEM VINDO AO SISTEMA DE OUVIDORIA!":>38}')
print('-=' * 20)


def divisoria():
    print('-' * 35)


selecionado = ocorre.Ocorrencia()

while i != 0:
    print('1 - Cadastrar Ocorrência')
    print('2 - Listar Ocorrência(s)')
    print('3 - Apagar Ocorrência(s)')
    print('0 - Sair')
    opcao = int(input('digite a opção desejada: '))
    if (opcao < 0) or (opcao > 3):
        print('Opção errada, tente novamente!')
        divisoria()
    else:
        if (opcao == 1):
            divisoria()
            print(f'{"MENU CATEGORIAS":>24}')
            divisoria()
            print('Categorias:')
            print('1 - Elogio ')
            print('2 - Reclamação')
            print('0 - Voltar')

            categoria = int(input('Escolha a categoria da sua ocorrência: '))

            while categoria < 0 or categoria > 2:
                print('Opção errada, tente novamente!')
                divisoria()
                categoria = int(input('Digite a opção desejada:'))
            if categoria == 0:
                divisoria()
            else:
                inserirOcorrencia = input('Digite sua opinião: ')
                selecionado.inserir(categoria, inserirOcorrencia)
                print('Sua opinião foi registrada!')
                divisoria()
        elif (opcao == 2):
            if (len(selecionado.elogio) == 0) and (len(selecionado.reclamacao) == 0):
                print('Ainda não possui ocorrência...')
                divisoria()
            else:
                divisoria()
                print(f'{"MENU LISTAS":>24}')
                divisoria()
                print('1 - Lista de Elogio(s)')
                print('2 - Lista de Reclamação(ões)')
                print('3 - Todas as Ocorrências')
                print('0 - Voltar')
                # listaMenu = [0, 1, 2, 3]
                listarTipo = int(input('Digite a opção desejada: '))
                while listarTipo < 0 or listarTipo > 3:
                    print('Opção errada, tente novamente!')
                    divisoria()
                    listarTipo = int(input('Digite a opção desejada: '))
                if (listarTipo == 1) and (len(selecionado.elogio) > 0):
                    divisoria()
                    print('Lista de Elogio(s):')
                    divisoria()
                    selecionado.listar(listarTipo)
                    divisoria()
                elif (listarTipo == 1) and (len(selecionado.elogio) == 0):
                    print('Ainda não possui elogio registrado.')
                    divisoria()
                elif (listarTipo == 2) and (len(selecionado.reclamacao) > 0):
                    divisoria()
                    print('Ocorrências de Reclamações:')
                    divisoria()
                    selecionado.listar(listarTipo)
                    divisoria()
                elif (listarTipo == 2) and (len(selecionado.reclamacao) == 0):
                    print('Ainda não possui reclamações registradas.')
                    divisoria()
                elif (listarTipo == 3):
                    divisoria()
                    print('Todas as ocorrências:')
                    divisoria()
                    selecionado.listar(listarTipo)
                    divisoria()
                else:
                    divisoria()
        elif (opcao == 3):
            if (len(selecionado.elogio) == 0) and (len(selecionado.reclamacao) == 0):
                print('Ainda não possui ocorrência para ser apagada!')
                divisoria()
            else:
                divisoria()
                print(f'{"MENU APAGAR":>24}')
                divisoria()
                print('1 - Apagar ocorrência especifica: ')
                print('2 - Apagar tudo')
                print('0 - Voltar')

                opcaoApagar = int(input('Digite a opção desejada:'))
                while opcaoApagar < 0 or opcaoApagar > 2:
                    print('Opção errada, tente novamente!')
                    divisoria()
                    opcaoApagar = int(input('Digite a opção desejada:'))
                if (opcaoApagar == 1):
                    print('1 - Apagar Elogio(os)')
                    print('2 - Apagar Reclamação(ões)')
                    print('0 - Voltar')
                    listarTipo = int(input('Digite a opção desejada: '))
                    while listarTipo < 0 or listarTipo > 3:
                        print('Opção errada, tente novamente!')
                        divisoria()
                        listarTipo = int(input('Digite a opção desejada: '))
                    if (listarTipo == 1) and (len(selecionado.elogio) > 0):
                        for x in range(len(selecionado.elogio)):
                            print('%d -> %s' % (x + 1, selecionado.elogio[x]))
                        opcaoApagando = int(input('Digite o indice que deseja apagar: '))
                        selecionado.apagar(listarTipo, opcaoApagando)
                        print('Ocorrência %d apagada com sucesso!' % opcaoApagando)
                        divisoria()
                    elif (listarTipo == 1) and (len(selecionado.elogio) == 0):
                        print('Ainda não possui elogio registrado.')
                        divisoria()
                    elif (listarTipo == 2) and (len(selecionado.reclamacao) > 0):
                        for x in range(len(selecionado.reclamacao)):
                            print('%d -> %s' % (x + 1, selecionado.reclamacao[x]))
                        opcaoApagando = int(input('Digite o indice que deseja apagar: '))
                        selecionado.apagar(listarTipo, opcaoApagando)
                        print('Ocorrência %d apagada com sucesso!' % opcaoApagando)
                        divisoria()
                    elif (listarTipo == 2) and (len(selecionado.reclamacao) == 0):
                        print('Ainda não possui reclamação registrada.')
                    else:
                        divisoria()
                elif (opcaoApagar == 2):
                    selecionado.apagar(opcaoApagar, opcaoApagar)
                    print('Todas as ocorrências foram apagadas!')
                    divisoria()
                else:
                    divisoria()
        elif (opcao == 0):
            print('-=' * 20)
            print(f'{"Seu atendimento foi finalizado!":>35}')
            print(f'{"Até mais!":>23}')
            print('-=' * 20)
            i = 0