from src.gen_function import analiseDeProximidade
import argparse


def main():
    ap = argparse.ArgumentParser()

    ap.add_argument('-lista', '--listaDeStrings',
                    default=['abacate', 'pera', 'uva', 'banana', 'maçã','repolho', 'uva', 'feijão', 'arroz']
                    ,
                    help='Lista de strings')

    args = vars(ap.parse_args())

    listaDeStrings = args['listaDeStrings']

    '''
    chamada de função que faz a analise de proximidade
    '''
    analise = analiseDeProximidade(listaDeStrings,'uva',2)

    print(analise)


if __name__ == '__main__':
    main()
