from src.gen_function import contadorDeStrigs
import csv


def pdf_to_list():
    result = ''
    return result


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
