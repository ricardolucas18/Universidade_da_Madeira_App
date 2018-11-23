# -*- coding: utf-8 -*-
"""
_author_    = "Ricardo Lucas"
_copyright_ = "Copyright 2018, ESTIG - IPBeja"
_version_   = "18:05 02/02/2018"
"""

import matplotlib.pyplot as plt
from db_creation import sexoCandidatura, opcaoCandidatura, notasAlunosColocados, Cursos
from app_creation import db
import random

import numpy as np

class graphics:
    '''
    Classe com def para produzir gráficos
    '''
    def sexo_colocados(self):
        '''
        Produz o Gráfico do género dos Colocodos
        :return: gráfico sexos
        '''
        plt.gcf().clear()
        masculino=0
        feminino=0
        for colocados, sexo in db.session.query(sexoCandidatura.colocados, sexoCandidatura.sexo):
            if(sexo=='Masculino'):
                masculino = masculino + colocados
            else:
                feminino = feminino + colocados


        slices = [masculino, feminino]
        activities = ['Masculino', 'Feminino']
        colors = ['c', 'r']

        plt.pie(slices,
                labels=activities,
                colors=colors,
                startangle=90,
                shadow=True,
                autopct='%1.1f%%')

        plt.title('Percentagem de Sexo dos Colocados\nAcessos 2015 e 2016 da 1º fase e 2º fase')

        return plt.savefig('static/sexos.png', bbox_inches='tight')

    def opcoes_curso(self):
        '''
        Profuz o gráfico das Opções do curso
        :return: return imagem gráfico
        '''
        plt.gcf().clear()
        candidatos_opacao1 = []
        candidatos_opacao2 = []
        candidatos_opacao3 = []
        candidatos_opacao4 = []
        candidatos_opacao5 = []
        candidatos_opacao6 = []
        candidatos_total = []
        bins = []

        for opcao_bd, candidatos_bd in db.session.query(opcaoCandidatura.opcao, opcaoCandidatura.candidatos):
            if not bins:
                bins.append(opcao_bd)

            elif max(bins) < opcao_bd:
                bins.append(opcao_bd)

            if opcao_bd==1:
                candidatos_opacao1.append(candidatos_bd)
            elif opcao_bd==2:
                candidatos_opacao2.append(candidatos_bd)
            elif opcao_bd==3:
                candidatos_opacao3.append(candidatos_bd)
            elif opcao_bd==4:
                candidatos_opacao4.append(candidatos_bd)
            elif opcao_bd==5:
                candidatos_opacao5.append(candidatos_bd)
            elif opcao_bd==6:
                candidatos_opacao6.append(candidatos_bd)

        n_candidatos1 = sum(candidatos_opacao1)
        n_candidatos2 = sum(candidatos_opacao2)
        n_candidatos3 = sum(candidatos_opacao3)
        n_candidatos4 = sum(candidatos_opacao4)
        n_candidatos5 = sum(candidatos_opacao5)
        n_candidatos6 = sum(candidatos_opacao6)

        candidatos_total.append(n_candidatos1)
        candidatos_total.append(n_candidatos2)
        candidatos_total.append(n_candidatos3)
        candidatos_total.append(n_candidatos4)
        candidatos_total.append(n_candidatos5)
        candidatos_total.append(n_candidatos6)


        plt.bar(bins, candidatos_total)
        plt.xlabel('Opcção da Canditadura')
        plt.ylabel('Número de Candidatos')
        plt.title('Numero de Candidatos para cada opção de candidatura\nAcessos 2015 e 2016 da 1º fase e 2º fase')
        return plt.savefig('static/opcoes.png', bbox_inches='tight')

    def distribuicaoAlunosColocados(self):
        '''
        Produz o Gráfico da Distribuição dos alunos
        :return: gráfico da Fistribuição dos alunos
        '''
        plt.gcf().clear()
        x_notasPrimeiraFaseQuinze = []
        x_notasSegundaFaseQuinze = []
        x_notasPrimeiraFaseDezasseis = []
        x_notasSegundaFaseDezasseis = []
        y_notasPrimeiraFaseQuinze = []
        y_notasSegundaFaseQuinze = []
        y_notasPrimeiraFaseDezasseis = []
        y_notasSegundaFaseDezasseis = []

        for nota_bd, acesso_id, quantidade in db.session.query(notasAlunosColocados.nota, notasAlunosColocados.acesso_id, notasAlunosColocados.quantidade):
            if(acesso_id == 1):
                x_notasPrimeiraFaseQuinze.append(nota_bd)
                y_notasPrimeiraFaseQuinze.append(quantidade)
            elif(acesso_id == 2):
                x_notasSegundaFaseQuinze.append(nota_bd)
                y_notasSegundaFaseQuinze.append(quantidade)
            elif(acesso_id == 3):
                x_notasPrimeiraFaseDezasseis.append(nota_bd)
                y_notasPrimeiraFaseDezasseis.append(quantidade)
            elif(acesso_id == 4):
                x_notasSegundaFaseDezasseis.append(nota_bd)
                y_notasSegundaFaseDezasseis.append(quantidade)

        plt.plot(x_notasPrimeiraFaseQuinze, y_notasPrimeiraFaseQuinze, label='1º Fase 2015')
        plt.plot(x_notasSegundaFaseQuinze, y_notasSegundaFaseQuinze, label='2º Fase 2015')
        plt.plot(x_notasPrimeiraFaseDezasseis, y_notasPrimeiraFaseDezasseis, label='1º Fase 2016')
        plt.plot(x_notasSegundaFaseDezasseis, y_notasSegundaFaseDezasseis, label='2º Fase 2016')

        plt.xlabel('Notas De Candidatura')
        plt.ylabel('Quantidade(Alunos)')
        plt.title('Distribuição das Notas de Candidaturas\ne quantidades de Alunos')
        plt.legend()
        return plt.savefig('static/distribuicoes.png')

    def professoresHabilitações(self):
        '''
        Produção da Habilitação dos professores
        :return: Gráfico da Habilitaçãodos Professores
        '''
        plt.gcf().clear()
        fig = plt.figure()
        xs=[]
        ys=[]
        for i in range(10):
            x = i
            y = random.randrange(10)

            xs.append(x)
            ys.append(y)

        ax1 = fig.add_subplot(211)

        ax2 = fig.subplot(212)

        ax1.plot(xs, ys)

        ax2.plot(xs, ys)






p = graphics()
p.sexo_colocados()
p.opcoes_curso()
p.distribuicaoAlunosColocados()

