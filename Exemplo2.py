#  -*- coding: utf-8 -*-

arq = open("C:\\ProjPython\\dados.csv", 'r')

texto = arq.readlines()
for linha in texto:
    print(linha)

arq.close()