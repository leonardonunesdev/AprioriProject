from efficient_apriori import apriori
import pandas as pd
import xlrd
import csv

"""Converte a base de dados de .xls para .csv"""
with xlrd.open_workbook('Base de dados.xls') as wb:
    sh = wb.sheet_by_index(0)
    with open('Base de dados.csv', 'w', newline="") as f:
        c = csv.writer(f)
        for r in range(sh.nrows):
            c.writerow(sh.row_values(r))
    
bancoDados = pd.read_csv("Base de dados.csv")
listaLinhasBancoDados = []

for index, linha in bancoDados.iterrows():
    listaLinhasBancoDados.append((linha["Nome"],
                                linha["Febre"],
                                linha["Tosse"],
                                linha["Falta ar e dificuldade respirar"],
                                linha["Dor"],
                                linha["Mal-estar generalizado"],
                                linha["Fraqueza"],
                                linha["Suor intenso"],
                                linha["Nausea e Vomito"],
                                str(int(linha["Pneumonia"]))))

itemsets, rules = apriori(listaLinhasBancoDados, min_support=0.5,  min_confidence=0.5)
print(rules)

print(bancoDados)

