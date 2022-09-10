i = 1
print('-=' * 20)
print(f'{"BEM VINDO AO SISTEMA DE OUVIDORIA!":>38}')
print('-=' * 20)
def divisoria():
    print('-' * 35)
"""def checagem(opcao):
    while opcao < 0 or opcao > (len(listaMenu))-1:
        print('Opção errada, tente novamente!')
        divisoria()
        opcao = int(input('Digite novamente: '))"""
class Ocorrencia:
    elogio = []
    reclamacao = []
    def inserir(self,categoria):
        if categoria == 1:
            self.elogio.append(inserirOcorrencia)
        elif categoria == 2:
            self.reclamacao.append(inserirOcorrencia)

    def apagar(self,listarTipo):
        if listarTipo == 1:
            del self.elogio[opcaoApagando - 1]
        elif listarTipo == 2:
            del self.reclamacao[opcaoApagando - 1]

selecionado = Ocorrencia()

while i != 0:
    print('1 - Cadastrar Ocorrência')
    print('2 - Listar Ocorrência(s)')
    print('3 - Apagar Ocorrência(s)')
    print('0 - Sair')
    opcao = int(input('digite a opção desejada: '))
    if (opcao < 0) or (opcao > 3) :
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
            #listaMenu = [0,1,2]
            categoria = int(input('Escolha a categoria da sua ocorrência: '))
            #checagem(categoria)
            while categoria < 0 or categoria > 2:
                print('Opção errada, tente novamente!')
                divisoria()
                categoria = int(input('Digite a opção desejada:'))
            if categoria == 0:
                divisoria()
            else:
                inserirOcorrencia = input('Digite sua opinião: ')
                selecionado.inserir(categoria)
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
                #listaMenu = [0, 1, 2, 3]
                listarTipo = int(input('Digite a opção desejada: '))
                while listarTipo < 0 or listarTipo > 3:
                    print('Opção errada, tente novamente!')
                    divisoria()
                    listarTipo = int(input('Digite a opção desejada: '))
                if (listarTipo == 1) and (len(selecionado.elogio) > 0):
                    divisoria()
                    print('Lista de Elogio(s):')
                    divisoria()
                    for x in range(len(selecionado.elogio)):
                        print('%d -> %s' % (x+1,selecionado.elogio[x]))
                        divisoria()
                elif (listarTipo == 1) and (len(selecionado.elogio) == 0):
                    print('Ainda não possui elogio registrado.')
                    divisoria()
                elif (listarTipo == 2) and (len(selecionado.reclamacao) > 0):
                    divisoria()
                    print('Ocorrências de Reclamações:')
                    divisoria()
                    for x in range(len(selecionado.reclamacao)):
                        print('%d -> %s' % (x+1,selecionado.reclamacao[x]))
                        divisoria()
                elif (listarTipo == 2) and (len(selecionado.reclamacao) == 0):
                    print('Ainda não possui reclamações registradas.')
                    divisoria()
                elif (listarTipo == 3):
                    divisoria()
                    print('Todas as ocorrências:')
                    divisoria()
                    for x in range(len(selecionado.elogio)):
                        print('Elogio(os) -> %s' % selecionado.elogio[x])
                        divisoria()
                    for x in range(len(selecionado.reclamacao)):
                        print('Reclamação(ões) -> %s' % (selecionado.reclamacao[x]))
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
                #listaMenu = [0, 1, 2]
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
                            print('%d -> %s' % (x+1, selecionado.elogio[x]))
                        opcaoApagando = int(input('Digite o indice que deseja apagar: '))
                        selecionado.apagar(listarTipo)
                        print('Ocorrência %d apagada com sucesso!' % opcaoApagando)
                        divisoria()
                    elif (listarTipo == 1) and (len(selecionado.elogio) == 0):
                        print('Ainda não possui elogio registrado.')
                        divisoria()
                    elif (listarTipo == 2) and (len(selecionado.reclamacao) > 0):
                        for x in range(len(selecionado.reclamacao)):
                            print('%d -> %s' % (x+1, selecionado.reclamacao[x]))
                        opcaoApagando = int(input('Digite o indice que deseja apagar: '))
                        selecionado.apagar(listarTipo)
                        print('Ocorrência %d apagada com sucesso!' % opcaoApagando)
                        divisoria()
                    elif (listarTipo == 2) and (len(selecionado.reclamacao) == 0):
                        print('Ainda não possui reclamação registrada.')
                    else:
                        divisoria()
                elif (opcaoApagar == 2):
                    for x in range(len(selecionado.elogio)):
                        del selecionado.elogio[x - 1]
                    for x in range(len(selecionado.reclamacao)):
                        del selecionado.reclamacao[x - 1]
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
