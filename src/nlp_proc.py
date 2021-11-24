import stanza

def pdf_to_list():
    result = ''
    return result

def stop_words():
    result = ''
    return result

def tokenizar(texto, idioma, quebrar_linha):
    '''
    Realiza a tokenização de um texto
    :param texto: Texto no qual será realizado a tokenização
    :param idioma: Idioma do texto
    :param quebrar_linha: Deve utilizar \n\n como quebra de linha. True = Sim, False = Não
    :return: Lista com as sentenças e seus respectivos tokens
    '''
    stanza.download(idioma)

    nlp = stanza.Pipeline(lang=idioma, processors='tokenize', tokenize_no_ssplit=quebrar_linha)

    doc = nlp(texto)

    result = []

    for i, sentence in enumerate(doc.sentences):
        result.append([sentence.text.lower(), [token.text.lower() for token in sentence.tokens]])

    return result

def lematizar():
    result = ''
    return result

def gerar_resultados():
    result = ''
    return result

def gerar_csv():
    result = ''
    return result

def gerar_mapa_palavras():
    result = ''
    return result