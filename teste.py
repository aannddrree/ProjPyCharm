arq = open("C:\\ProjPython\\dados.csv","rb")
texto = arq.readlines()

for linha in texto:
    if "PORTLAND" in str(linha):
        print(linha)
arq.close()