class Ocorrencia:
    elogio = []
    reclamacao = []
    def inserir(self,categoria,inserirOcorrencia):
        if categoria == 1:
            self.elogio.append(inserirOcorrencia)
        elif categoria == 2:
            self.reclamacao.append(inserirOcorrencia)

    def listar(self,listarTipo):
        if listarTipo == 1:
            for x in range(len(self.elogio)):
                print('%d -> %s' % (x + 1, self.elogio[x]))
        elif listarTipo == 2:
            for x in range(len(self.reclamacao)):
                print('%d -> %s' % (x + 1, self.reclamacao[x]))
        elif listarTipo == 3:
            for x in range(len(self.elogio)):
                print('Elogio(os) -> %s' % self.elogio[x])

            for x in range(len(self.reclamacao)):
                print('Reclamação(ões) -> %s' % (self.reclamacao[x]))

    def apagar(self,listarTipo,opcaoApagando):
        if listarTipo == 1:
            if listarTipo == 1:
                del self.elogio[opcaoApagando - 1]
            elif listarTipo == 2:
                del self.reclamacao[opcaoApagando - 1]
        elif listarTipo == 2:
            for x in range(len(self.elogio)):
                del self.elogio[x - 1]
            for x in range(len(self.reclamacao)):
                del self.reclamacao[x - 1]