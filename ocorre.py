import mysql.connector

class Ocorrencia:

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ouvidoria'
    )

    cursor = connection.cursor()

    def inserir(self,categoria,inserirOcorrencia):
        if categoria == 1:
            elogio = 'insert into ocorrencias (id,ocorrencia,tipo) value (%s,%s,%s)'
            dados = ('default', f'{inserirOcorrencia}','Elogio')
            self.cursor.execute(elogio,dados)
            self.connection.commit()
        elif categoria == 2:
            reclamacao = 'insert into ocorrencias (id,ocorrencia,tipo) value (%s,%s,%s)'
            dados = ('default', f'{inserirOcorrencia}','Reclamação')
            self.cursor.execute(reclamacao, dados)
            self.connection.commit()
    def listar(self,listarTipo):
        if listarTipo == 1:
            sqlE = 'select * from ocorrencias where tipo = "Elogio"'
            self.cursor.execute(sqlE)
            listaElogios = self.cursor.fetchall()
            for elogios in listaElogios:
                print('%d -> %s' % (elogios[0], elogios[1]))

        elif listarTipo == 2:
            sqlR = 'select * from ocorrencias where tipo = "Reclamação"'
            self.cursor.execute(sqlR)
            listaReclamacao = self.cursor.fetchall()
            for reclamacao in listaReclamacao:
                print('%d -> %s' % (reclamacao[0], reclamacao[1]))
        elif listarTipo == 3:
            sql = ' select * from ocorrencias'
            self.cursor.execute(sql)
            listaTodos = self.cursor.fetchall()
            for todos in listaTodos:
                print('%d -> %s (%s)' % (todos[0],todos[1],todos[2]))
            #sqlR = ' select * from reclamação'
           # self.cursor.execute(sqlR)
            #listaReclamacao = self.cursor.fetchall()
            #for reclamacao in listaReclamacao:
                #print('Reclamação -> %s' % (reclamacao[1]))

    def apagar(self,listarTipo,opcaoApagando):
        if listarTipo == 1:
            #if listarTipo == 1:
            sql = f'Delete from ocorrencias where id = {opcaoApagando}'
            self.cursor.execute(sql)
            self.connection.commit()
            #elif listarTipo == 2:
                #sqlR = f'Delete from ocorrencias where id = {opcaoApagando}'
                #self.cursor.execute(sqlR)
                #self.connection.commit()
        elif listarTipo == 2:
            apagarTudo = 'truncate table ocorrencias'
            self.cursor.execute(apagarTudo)
            self.connection.commit()

    def verificar(self,parametro):

        sqlE = 'select count(tipo) from ocorrencias where tipo = "Elogio"'
        self.cursor.execute(sqlE)
        listaElogio = self.cursor.fetchall()
        sqlR = 'select count(tipo) from ocorrencias where tipo = "Reclamação"'
        self.cursor.execute(sqlR)
        listaReclamacao = self.cursor.fetchall()

        for elogios in listaElogio:
            quantidadeElogios = elogios[0]
        for reclamacao in listaReclamacao:
            quantidadeReclamacao = reclamacao[0]

        if parametro == 1:
            if quantidadeReclamacao == 0 and quantidadeElogios == 0:
                return True
            else:
                return False
        elif parametro == 2:
            if quantidadeElogios == 0:
                return True
            else:
                return False
        elif parametro == 3:
            if quantidadeReclamacao == 0:
                return True
            else:
                return False






