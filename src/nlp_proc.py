from PyPDF2 import PdfFileReader
import csv
import stanza
import pandas as pd
import collections
import os
import numpy as np
import string
import nltk
import re
import fitz

# Download Port language model and initialize the NLP
stanza.download('pt')
nlp = stanza.Pipeline('pt')
nltk.download('stopwords')

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

    palavras_pagina = []

    textointeiro = ""

  
    with fitz.open(caminho_pdf) as pdf:
        for pagina in pdf:
            textointeiro += pagina.getText()

    textointeiro = textointeiro.strip()
    textointeiro = textointeiro.replace("\n"," ")
    textointeiro = textointeiro.replace("\t"," ")
    textointeiro = re.sub(' +',' ', textointeiro)
    textointeiro = re.sub(r'[0-9]+','', textointeiro)
    textointeiro = re.sub(r'[.()/%]+','', textointeiro)
    palavras_pagina = textointeiro.split()

    return textointeiro,palavras_pagina

def word_info_df(doc):
    """
    - Parameters: doc (a Stanza Document object)
    - Returns: A Pandas DataFrame object with one row for each token in
      doc, and columns for text, lemma, upos, and xpos.
    """
    rows = []
    for sentence in doc.sentences:
        for word in sentence.words:
            #if word not in lista_stop_words
            row = {
                    "text": word.text,
                    "lemma": word.lemma,
                    "upos": word.upos,
                    "xpos": word.xpos,
                }
            rows.append(row)
    
    return rows



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


def tokenizar(texto,nlp):
    '''
    Realiza a tokenização de um texto
    :param texto: String no qual será realizado a tokenização
    :param idioma: String informando o idioma do texto
    :param quebrar_linha: Boleano informando se deve utilizar \n\n como quebra de linha. True = Sim, False = Não
    :return: Dataframe com as sentenças e seus respectivos tokens
    '''


    doc = nlp(texto)

    tokens = []

    for i, sentence in enumerate(doc.sentences):
        tokens.append([sentence.text.lower(),
                      [token.text.lower() for token in sentence.tokens]])
        

    return pd.DataFrame(tokens, columns=['sentenca','tokens'])


def lematizar(df):
    """
    Função para fazer o processo de lematização dos textos
    => lematizar: agrupar diferentes formas da mesma palavra
        exemplo: 'correr', 'corre', 'correu' mesmo lema => 'correr'
    entrada: texto
    saída: Objeto de document
    importante: precisa da biblioteca stanza
    """
    
    df_lema = []
    for i, r in df.iterrows():
        
        texto_lem =  nlp(df.iloc[i, 3])
        
        df_lema +=  word_info_df(texto_lem)
        #if i == 0: break
    
     
    return pd.DataFrame(df_lema) #se for dataframe

def pre_processamento(texto, idioma, quebrar_linha, lista_stop_words, pontuacao):
    '''
    Realiza o pré-processamento do documento (tokenização e remoção de stop words, deixar todos os caracteres minúsculos
    :param paginas: Lista com as páginas do documento, onde cada posição da lista é o texto de uma página
    :param idioma: String informando o idioma do texto
    :param quebrar_linha: Boleano informando se deve utilizar \n\n como quebra de linha. True = Sim, False = Não
    :return: Lista de dataframe com o resultado do processamento das páginas. Cada elemento da lista contém 1 dataframe correspondente ao resultado do processamento de 1 página
    '''
    #result = []
    nlp = stanza.Pipeline(lang=idioma, processors='tokenize', tokenize_no_ssplit=quebrar_linha)
    #for pagina in paginas:
    df = tokenizar(texto,nlp)
    df['sem_stop_words'] = None
    df['texto_sem_stop_words'] = None
   
    for i, r in df.iterrows():
        df.iloc[i, 2] = stop_words(r['tokens'],
                                    lista_stop_words,
                                    pontuacao)
        df.iloc[i, 3] = ' '.join(df.iloc[i, 2])
        

    return df


def gerar_TF(listLematizacao):
    '''
    Term Frequency (TF):
    𝑇𝐹 = quantidade de ocorrência de um termo em um texto / quantidade total de palavras do texto
    '''

    TF = []
    for _listLematizacao in listLematizacao:
        pdftexto = _listLematizacao['text'].tolist()
        dicOcorrenciapalavra = collections.Counter(pdftexto)
        lenght = len(pdftexto)
        
        for palavra in dicOcorrenciapalavra:
            dicOcorrenciapalavra[palavra] /= lenght
        TF.append(dicOcorrenciapalavra)


    
    return TF


def gerar_DF(listLematizacao):
    '''
    Document Frequency (DF)
    𝐷𝐹 = quantidade de ocorrência de um termo em um conjunto de documentos 
    '''

    TF = gerar_TF(listLematizacao)
    palavrastodospdfs = []
    
    for _listLematizacao in listLematizacao:
        palavrastodospdfs += _listLematizacao['text'].tolist()

    DF = collections.Counter(palavrastodospdfs)

    return DF,TF


def gerar_IDF(listLematizacao,numero_documentos):
    '''
    Inverse Document Frequency (IDF)
    𝐼𝐷𝐹 = log(quantidade de documentos / (𝐷𝐹+1))
    '''
    DF,TF = gerar_DF(listLematizacao)

    for _listLematizacao in listLematizacao:
        for palavra in _listLematizacao['text'].tolist():
            DF[palavra] +=  np.log(numero_documentos /(DF[palavra] + 1))  
    
    
    return TF,DF #  TF,IDF

def gerar_TFIDF(listLematizacao,numero_documentos):
    TF,IDF = gerar_IDF(listLematizacao,numero_documentos)
    
    TFIDF = IDF # iniciando variavel como cópia

    for _tf in TF:
        for palavra in _tf:
            TFIDF[palavra] += _tf[palavra] * IDF[palavra]

    return TFIDF


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


TF_list = []
documentos_dir = "src\\NLPData"


listLematizacao = []
lista_stop_words = nltk.corpus.stopwords.words('portuguese')


dir_list = os.listdir(documentos_dir)
numero_documentos = len(dir_list)
for filename in dir_list:
    f = os.path.join(documentos_dir, filename)
    if os.path.isfile(f):
        resulttextcompleto,pdfpalavraslist = pdf_to_list(f)
        result = pre_processamento(resulttextcompleto,"pt" , False, lista_stop_words , string.punctuation)       
        res = lematizar(result)
        listLematizacao.append(res)

      

TFIDF_text = gerar_TFIDF(listLematizacao,numero_documentos)

df = pd.DataFrame.from_records(list(dict(TFIDF_text).items()), columns=['token','TFIDF'])
df.to_csv("arquivo_.csv", sep=';')