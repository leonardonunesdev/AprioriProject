import pyfpgrowth
import pandas as pd

bancoDados = pd.read_csv("Base de dados.csv")
listaLinhasBancoDados = []

for index, linha in bancoDados.iterrows():
    listaLinhasBancoDados.append([linha["Nome"],
                                linha["Febre"],
                                linha["Tosse"],
                                linha["Falta ar e dificuldade respirar"],
                                linha["Dor"],
                                linha["Mal-estar generalizado"],
                                linha["Fraqueza"],
                                linha["Suor intenso"],
                                linha["Nausea e Vomito"],
                                str(int(linha["Pneumonia"]))])

padroes = pyfpgrowth.find_frequent_patterns(listaLinhasBancoDados, 250)
""" print(padroes) """

regras = pyfpgrowth.generate_association_rules(padroes, 1)
""" print(regras) """


for regra in regras:
    print(regra)




    