ocorrenciasInternet = []
ocorrenciasTv =[]
i = 1
print('-=' * 20)
print('   BEM VINDO AO SISTEMA DE OUVIDORIA!')
print('-=' * 20)
while i != 0:
    print('1 - Cadastrar Ocorrência')
    print('2 - Listar Ocorrência(s)')
    print('3 - Apagar Ocorrência(s)')
    print('0 - Sair')
    opcao = int(input('digite a opção desejada: '))
    if (opcao < 0) or (opcao > 3) :
        print('Opção errada, tente novamente!')
        print('-' * 35)
    else:
        if (opcao == 1):
            print('Categorias:')
            print('1 - Internet ')
            print('2 - Tv a cabo')
            print('3 - Voltar')
            categoria = int(input('Escolha a categoria da sua ocorrência: '))
            if (categoria == 1):
                print('Bem vindo a sua ouvidoria da sua internet!')
                inserirOcorrenciaInternet = input('Digite sua ocorrência: ')
                ocorrenciasInternet.append(inserirOcorrenciaInternet)
                print('Ocorrência cadastrada!')
                print('-' * 35)
            elif (categoria == 2):
                print('Bem vindo a sua ouvidoria da sua TV!')
                inserirOcorrenciaTv = input('Digite sua ocorrência: ')
                ocorrenciasTv.append(inserirOcorrenciaTv)
                print('Ocorrência cadastrada!')
                print('-' * 35)
            else:
                print('-' * 35)
        elif (opcao == 2):
            if (len(ocorrenciasInternet) == 0) and (len(ocorrenciasTv) == 0):
                print('Ainda não possui ocorrência...')
                print('-' * 35)
            else:
                print('1 - Ocorrências de internet')
                print('2 - Ocorrências de Tv')
                print('3 - Todas as ocorrências')
                print('4 - Voltar')
                listarTipo = int(input('Digite a opção desejada: '))
                if (listarTipo == 1) and (len(ocorrenciasInternet) > 0) :
                    print('Ocorrências de internet:')
                    for x in range(len(ocorrenciasInternet)):
                        print('%d -> %s' % (x+1,ocorrenciasInternet[x]))
                        print('-' * 35)
                elif (listarTipo == 1) and (len(ocorrenciasInternet) == 0):
                    print('Ainda não possui ocorrências de internet registradas.')
                elif (listarTipo == 2) and (len(ocorrenciasTv) > 0):
                    print('Ocorrências de Tv:')
                    for x in range(len(ocorrenciasTv)):
                        print('%d -> %s' % (x+1,ocorrenciasTv[x]))
                        print('-' * 35)
                elif (listarTipo == 2) and (len(ocorrenciasTv) == 0):
                    print('Ainda não possui ocorrências de Tv registradas.')
                elif (listarTipo == 3):
                    print('Todas as ocorrências:')
                    for x in range(len(ocorrenciasInternet)):
                        print('Internet -> %s' % ocorrenciasInternet[x])
                        print('-' * 35)
                    for x in range(len(ocorrenciasTv)):
                        print('Tv -> %s' % ocorrenciasTv[x])
                        print('-' * 35)
                else:
                    print('-' * 35)
        elif (opcao == 3):
            if (len(ocorrenciasInternet) == 0) and (len(ocorrenciasTv) == 0):
                print('Ainda não possui ocorrência para ser apagada!')
                print('-' * 35)
            else:
                print('1 - Apagar ocorrência especifica: ')
                print('2 - Apagar tudo')
                print('3 - Voltar')
                opcaoApagar = int(input())
                if (opcaoApagar == 1):
                    print('1 - Apagar ocorrências de internet')
                    print('2 - Apagar ocorrências de Tv')
                    print('3 - Voltar')
                    listarTipo = int(input('Digite a opção desejada: '))
                    if (listarTipo == 1) and (len(ocorrenciasInternet) > 0):
                        for x in range(len(ocorrenciasInternet)):
                            print('%d -> %s' % (x+1, ocorrenciasInternet[x]))
                        opcaoApagando = int(input('Digite o indice que deseja apagar: '))
                        del ocorrenciasInternet[opcaoApagando-1]
                        print('Ocorrência %d apagada com sucesso!' % opcaoApagando)
                        print('-' * 35)
                    elif (listarTipo == 1) and (len(ocorrenciasInternet) == 0):
                        print('Ainda não possui ocorrências de internet registradas.')
                    elif (listarTipo == 2) and (len(ocorrenciasTv) > 0):
                        for x in range(len(ocorrenciasTv)):
                            print('%d -> %s' % (x+1, ocorrenciasTv[x]))
                        opcaoApagando = int(input('Digite o indice que deseja apagar: '))
                        del ocorrenciasTv[opcaoApagando-1]
                        print('Ocorrência %d apagada com sucesso!' % opcaoApagando)
                        print('-' * 35)
                    elif (listarTipo == 2) and (len(ocorrenciasTv) == 0):
                        print('Ainda não possui ocorrências de Tv registradas.')
                    else:
                        print('-' * 35)
                elif (opcaoApagar == 2):
                    for x in range(len(ocorrenciasInternet)):
                        del ocorrenciasInternet[x-1]
                    for x in range(len(ocorrenciasTv)):
                        del ocorrenciasTv[x-1]
                    print('Todas as ocorrências foram apagadas!')
                    print('-' * 35)
                else:
                    print('-' * 35)
        elif (opcao == 0):
            print('Seu atendimento foi finalizado!')
            print('Até mais!')
            i = 0
