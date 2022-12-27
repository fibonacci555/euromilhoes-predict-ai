import scraper
from openpyxl import Workbook



def start(filename):
    sheettitle = 'Numeros'

    for i in range(2009, 2023):
        scraper.readAll(i)
    wb = Workbook()
    wb['Sheet'].title = sheettitle
    sh1 = wb.active
    sh1['A1'].value = 'ID'
    sh1['B1'].value = 'Numero1'
    sh1['C1'].value = 'Numero2'
    sh1['D1'].value = 'Numero3'
    sh1['E1'].value = 'Numero4'
    sh1['F1'].value = 'Numero5'
    sh1['G1'].value = 'Estrela1'
    sh1['H1'].value = 'Estrela2'
    sh1['I1'].value = 'Numero Completo'

    for i in range(len(scraper.numeros_full)):

        sh1[f'A{str(2+i)}'].value = str(scraper.numeros_full[i][0])
        sh1[f'B{str(2+i)}'].value = str(scraper.numeros_full[i][1])
        sh1[f'C{str(2+i)}'].value = str(scraper.numeros_full[i][2])
        sh1[f'D{str(2+i)}'].value = str(scraper.numeros_full[i][3])
        sh1[f'E{str(2+i)}'].value = str(scraper.numeros_full[i][4])
        sh1[f'F{str(2+i)}'].value = str(scraper.numeros_full[i][5])
        sh1[f'G{str(2+i)}'].value = str(scraper.numeros_full[i][6])
        sh1[f'H{str(2+i)}'].value = str(scraper.numeros_full[i][7])
        sh1[f'I{str(2+i)}'].value = sh1[f'B{str(2+i)}'].value + sh1[f'C{str(2+i)}'].value + sh1[f'D{str(2+i)}'].value + sh1[f'E{str(2 + i)}'].value + sh1[f'F{str(2+i)}'].value + sh1[f'g{str(2+i)}'].value + sh1[f'H{str(2+i)}'].value







    try:
        wb.save(filename)
    except PermissionError:
        print('File might be opened, please close it before writing')