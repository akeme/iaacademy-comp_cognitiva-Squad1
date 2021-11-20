from PyPDF2 import PdfFileReader
import csv

def pdf_to_list(caminho_pdf):
    """
        função que extrai as palavras de um pdf
        :param caminho_pdf: caminho do pdf para a extração das palavras
        :return: retorna uma lista com as palavras extraidas do pdf
        """
    # abre o pdf
    pdf = PdfFileReader(open(caminho_pdf, "rb"))

    # inicializa lista com as paginas
    lista_paginas = []

    for page in range(0, pdf.getNumPages()):
        pagina_atual = pdf.getPage(page)
        texto = pagina_atual.extractText()
        palavras_pagina = texto.split()
        lista_paginas.append(palavras_pagina)

    return lista_paginas

def stop_words():
    result = ''
    return result


def tokenizar():
    result = ''
    return result


def lematizar():
    result = ''
    return result


def gerar_resultados():
    result = ''
    return result


def gerar_csv(document_list: list):
    # csv header
    fieldnames = ['Token', 'TF', 'DF', 'IDF', 'TF-IDF']

    with open('documents.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(document_list)

    result = 'documents.csv'
    return result


def gerar_mapa_palavras():
    result = ''
    return result
