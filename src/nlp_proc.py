from PyPDF2 import PdfFileReader
import csv
import stanza
import pandas as pd
import collections
import os
import numpy as np

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

    textointeiro = ""

    for page in range(0, pdf.getNumPages()):
        pagina_atual = pdf.getPage(page)
        texto = pagina_atual.extractText()
        textointeiro += texto
        palavras_pagina = texto.split()
        lista_paginas.append(palavras_pagina)

    return lista_paginas,textointeiro

def pre_processamento(paginas, idioma, quebrar_linha, lista_stop_words, pontuacao):
    '''
    Realiza o pré-processamento do documento (tokenização e remoção de stop words, deixar todos os caracteres minúsculos
    :param paginas: Lista com as páginas do documento, onde cada posição da lista é o texto de uma página
    :param idioma: String informando o idioma do texto
    :param quebrar_linha: Boleano informando se deve utilizar \n\n como quebra de linha. True = Sim, False = Não
    :return: Lista de dataframe com o resultado do processamento das páginas. Cada elemento da lista contém 1 dataframe correspondente ao resultado do processamento de 1 página
    '''
    result = []

    for pagina in paginas:
        df = tokenizar(pagina, idioma, quebrar_linha)

        df['sem_stop_words'] = None

        for i, r in df.iterrows():
            df.iloc[i, 2] = stop_words(r['tokens'],
                                       lista_stop_words,
                                       pontuacao)

        result.append(df)

    return result

def stop_words(tokens, lista_stop_words, pontuacao):
    '''
    Realiza a remoção de stop words e pontuação
    :param tokens: Lista de tokens extraídos das sentenças
    :param lista_stop_words: Lista de stop words a ser removida da lista de tokens
    :param pontuacao: Lista de pontuação a ser removida da lista de tokens
    :return: Lista com de tokens sem stop words e sem pontuação
    '''

    #Remove stop words
    result = [t for t in tokens if t not in lista_stop_words]

    #Remove pontuação
    result = [t for t in result if t not in pontuacao]

    return result

def tokenizar(texto, idioma, quebrar_linha):
    '''
    Realiza a tokenização de um texto
    :param texto: String no qual será realizado a tokenização
    :param idioma: String informando o idioma do texto
    :param quebrar_linha: Boleano informando se deve utilizar \n\n como quebra de linha. True = Sim, False = Não
    :return: Dataframe com as sentenças e seus respectivos tokens
    '''

    nlp = stanza.Pipeline(lang=idioma, processors='tokenize', tokenize_no_ssplit=quebrar_linha)

    doc = nlp(texto)

    tokens = []

    for i, sentence in enumerate(doc.sentences):
        tokens.append([sentence.text.lower(),
                      [token.text.lower() for token in sentence.tokens]])

    return pd.DataFrame(tokens, columns=['sentenca','tokens'])

def lematizar():
    result = ''
    return result

def gerar_TF(s_Texto):
    '''
    Term Frequency (TF):
    𝑇𝐹 = quantidade de ocorrência de um termo em um texto / quantidade total de palavras do texto
    '''

    TF = []

    dicOcorrenciapalavra = collections.Counter(s_Texto.split())
    lenght = len(s_Texto.split())

    for palavra in dicOcorrenciapalavra:
        dicOcorrenciapalavra[palavra] /= lenght
    
    TF.append(dicOcorrenciapalavra)
    
    return TF


def gerar_DF(documentos_dir = "src\\NLPData"):
    '''
    Document Frequency (DF)
    𝐷𝐹 = quantidade de ocorrência de um termo em um conjunto de documentos 
    '''
    dir_list = os.listdir(documentos_dir)
    DF = []
    for filename in os.listdir(dir_list):
        f = os.path.join(documentos_dir, filename)
        if os.path.isfile(f):
            pdflist,textointeiro = pdf_to_list(f)
            dicOcorrenciapalavra = collections.Counter(textointeiro.split())
            DF.append(dicOcorrenciapalavra)
    
    return DF,len(dir_list)


def gerar_IDF():
    '''
    Inverse Document Frequency (IDF)
    𝐼𝐷𝐹 = log(quantidade de documentos / (𝐷𝐹+1))
    '''
    DF,numerodearquivos = gerar_DF("src\\NLPData")
    
    for index in range(len(DF)):
        for palavra in DF[index]:
            DF[index][palavra] = np.log(numerodearquivos /(DF[index][palavra] + 1))
    
    return DF # DF modificado



def gerar_TFIDF():
    '''
    TF-IDF
    𝑇𝐹−𝐼𝐷𝐹 = 𝐼𝐷𝐹 * 𝑇𝐹
    '''
    IDF = gerar_IDF()
    TF = gerar_TF("s_Texto")



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
