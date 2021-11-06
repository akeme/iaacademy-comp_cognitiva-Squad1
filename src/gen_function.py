# exercicio 01 da aula 02
import math
import numpy as np
import collections
#funcao para calcular distancia
def calcularDistancia(p1,p2):
    """
    formula para calcular a distancia entre 2 pontos
    entradas:
    p1 - primeiro ponto: array numpy contento as coordenadas do primeiro ponto
    p2 - segundo ponto : array numpy contento as coordenadas do segundo ponto

    saida:
     distancia euclidiana dos pontos
    """

    distancia = np.linalg.norm(p1 - p2)
    # retornando o valor da distancia
    return distancia

def buscaPontoProximo (listaDePontos, pontoAlvo):

    distanciaPonto = None
    distanciaPontoProximo = float('inf')
    print(distanciaPontoProximo)

    for ponto in listaDePontos:
        distanciaAtual = calcularDistancia(pontoAlvo, ponto)

        if distanciaAtual < distanciaPontoProximo:
            distanciaPontoProximo = distanciaAtual
            distanciaPonto = ponto

    return distanciaPonto



def contadorDeStrigs(listaStrings):
    '''
    :param listaStrings: recebe uma lista de palavras
    :return: retorna as palavras e a quantidade que cada uma na lista
    '''
    contadorString = {}
    for palavra in set(listaStrings):
        cont = listaStrings.count(palavra)
        contadorString[palavra] = cont
    return contadorString



def analiseDeProximidade(listaPalavra, palavra,limiarDeAnalise):
    '''

    :param listaPalavra: lista de palavras para fazer a busca
    :param palavra: palavras de busca na lista
    :param limiarDeAnalise: numero de proximidade
    :return: lista com as palavas de proximidade
    '''

    #cria um array numpy ndarray
    array = np.array(listaPalavra)
    # retorna o(s) indice(s) da palavra de busca
    a = np.where(array == palavra)
    #lista com o(s) indice(s)
    listaindices = a[0]
    #criacao da lista de retonro
    listaDeretorno = []
    for indice in listaindices:
        # limita o indice do inicio da lista
        if (indice - limiarDeAnalise<0):
            inicio = 0
        else:
            inicio = indice - limiarDeAnalise

        # limita o indice de fim da lista
        if (indice + limiarDeAnalise + 1 > len(listaPalavra)):
            listaTemporaria = listaPalavra[inicio:]
        else:
            fim = indice + limiarDeAnalise + 1
            listaTemporaria = listaPalavra[inicio:fim]
        #adicionando elemento a lista de retorno
        listaDeretorno = listaDeretorno + listaTemporaria
        #removendo palavras de busca
        listaDeretorno.remove(palavra)
    return listaDeretorno


def retornalistarepetidos(lista):
    """
    função que retorna itens repetidos de um lista
    entradas:
    lista: array numpy contento as coordenadas do primeiro ponto

    saida:
     lista com os valores repetidos na lista informada
    """
    y = collections.Counter(lista)
    return [i for i in y if y[i] > 1]

def ordenalista(lista, crescente):
    """
    função ordenar uma lista baseada na quantidade de elementos de cada string

    entrada:
    lista: lista a ser ordenada
    crescente: tipo booleano ser ordenava a lista crescente

    saida:
    retorna uma lista ordenada ou não
    """
    for i in range(len(lista) - 1, 0, -1):
        for indice in range(i):
            if len(lista[indice]) > len(lista[indice + 1]):
                aux = lista[indice]
                lista[indice] = lista[indice + 1]
                lista[indice + 1] = aux

    return sorted(lista, key=len, reverse=crescente)

def Create_ROI(_Matrix,_ROI_Center_Cordinates,_ROIsize):
    '''

    :param _Matrix: The Matrix to be processed
    :param _ROI_Center_Cordinates: Center points coordinates for ROI
    :param _ROIsize: Size of ROI
    :return: A matrix resulting
    '''
    radius = int(_ROIsize/2)
    ROI_matrix = np.zeros((_ROIsize, _ROIsize), np.uint8)
    i=0
    j=0

    for x in range(_ROI_Center_Cordinates[0] - radius,_ROI_Center_Cordinates[0] + radius + 1):
        for y in range(_ROI_Center_Cordinates[1] - radius, _ROI_Center_Cordinates[1] + radius + 1):
            #Check Corners
            if(x > _Matrix.shape[0] or x < 0):
                continue
            if (y > _Matrix.shape[1] or y < 0):
                continue
            ROI_matrix[i][j] = _Matrix[x][y]
            j+=1
        i+=1
        j=0

    return ROI_matrix

def Create_Multiples_ROI(_Matrix,_ROI_Center_Cordinates_list,_ROIsize_list):
    '''

    :param _Matrix: The Matrix to be processed
    :param _ROI_Center_Cordinates_list: List with center points of coordinates for ROIs
    :param _ROIsize_list:
    :return: A list of matrix resulting
    '''
    if(len(_ROI_Center_Cordinates_list)!=len(_ROIsize_list)):
        raise ValueError('_ROI_Center_Cordinates_list and _ROIsize_list has different sizes ')

    ROI_list = []
    for i in range(len(_ROI_Center_Cordinates_list)):
        ROI_list.append(Create_ROI(_Matrix, _ROI_Center_Cordinates_list[i], _ROIsize_list[i]))

    return ROI_list

def maisProx(p, lp):
    """
        calcula o ponto mais próximo à 'p' dentre uma lista de pontos 'lp'
        :param p        ->  coordenda do qual se quer determinar a mais próxima
        :param lp       -> lista de coordenadas (lista de listas) cujos elementos serão testados pela função
        para se determinar a mais próximo de p
        :return prox    -> coordenada do ponto mais próximo à p
    """
    p = np.array(p)
    lp = np.array(lp)
    # inicializa a distância com infinito
    dist = np.inf
    # iniciliza o ponto mais próximo com o primeiro elemento da lista
    prox = lp[0]
    # itera os elementos da lita de coordendas
    for i in lp:
        # se achar um ponto com uma distância menor, este vai ser o mais próximo
        if distEucl(p, i) < dist:
            prox = i
    return prox


def distEucl(p1, p2):
    """
        calcula a distancia euclidiana entre dois pontos 'p1' e 'p2'
        :param p1       -> coordenda do primeiro ponto (o vetor pode ter dimensão qualquer)
        :param p2       -> coordenda do segundo ponto (o vetor pode ter dimensão qualquer)
        :return dist    -> distância euclidiana
    """
    p1 = np.array(p1)
    p2 = np.array(p2)

    dist = np.linalg.norm(p1-p2)
    return dist



def remover_duplicados(lista) :
    '''
    Função responsável por indentificar elementos duplicados em uma lista
    :param lista: Lista de elementos
    :return: Lista de elementos duplicados
    '''
    return list(dict.fromkeys(lista))

def limiar_array(matriz, limiar):
    '''
    Função responsável por binarização com limiar
    :param matriz: Matriz do tipo list de list [[],[],[]...]
    :param limiar: Limiar para binarização
    :return: Array binarizado
    '''
    array = np.array(matriz)

    array[array < limiar] = 0
    array[array != 0] = 1

    return array.tolist()

def repeticao_string(string,substring):
    '''
    função que determina a quantidade de repeticoes de uma strig dentro de uma lista de string

    entrada:
        string:
        substring:

    retorno:
        quantidade de repeticoes de uma string
    '''
    return string.count(substring)

def roi(mat, pt, tam):
    """
        retorna a Região de Interesse (ROI) de uma matriz dado a coordenada do ponto central 'pt' e o seu tamanho 'tam'
        :param mat      ->  matriz de dados
        :param pt       -> coordenada do ponto central da ROI
        :param tam      -> tamanho ao redor do ponto central da ROI
        :return _roi    -> matriz com a ROI
    """
    # se a coordenada do ponto central está fora da matriz, retorne uma matriz vazia
    if (pt[0] < 0) or (pt[0] > mat.shape[0] - 1) or (pt[1] < 0) or (pt[1] > mat.shape[1] - 1):
        return []
    # se o tamanho da ROI for incompatível com as dimensões da matriz, chame a função com um tamanho de ROI menor
    # e retorne a ROI
    elif (pt[0] - int(tam) < 0) or (pt[0] + int(tam) > mat.shape[0] - 1) or (pt[1] - int(tam) < 0) or (pt[1] + int(tam) > mat.shape[1] - 1):
        _roi = roi(mat, pt, tam-1)
        return _roi
        # roi = mat[(pt[0] - int(tam)):(pt[0] + int(tam) + 1), (pt[1] - tam):(pt[1] + tam + 1)]
    _roi = mat[(pt[0] - int(tam)):(pt[0] + int(tam) + 1), (pt[1] - tam):(pt[1] + tam + 1)]
    return _roi


def multiRoi(mat, pts, tams):
    """
        retorna multiplas Regiões de Interesse (ROI) de uma matriz dadas as coordenadas dos pontos centrais
        'pts' e o seus tamanhos 'tams'
        :param mat      ->  matriz de dados
        :param pts      -> coordenadas dos pontos centrais das ROIs
        :param tams     -> tamanhos ao redor dos pontos centrais das ROIs
        :return rois     -> matrizes com as ROIs
    """
    rois = []
    for i in range(len(pts)):
        rois.append(roi(mat, pts[i], tams[i]))

    return rois