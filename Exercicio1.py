import xlrd
book = xlrd.open_workbook("C:\\ProjPython\\1617FedSchoolCodeList.xlsx")
print("Número de abas: " + str(book.nsheets))
print("Nomes das Planilhas:" + str(book.sheet_names()))
sh = book.sheet_by_index(0)
print("Valor da célula D30 é " + sh.cell_value(rowx=29, colx=3))
for rx in range(sh.nrows):
    print(sh.row(rx))