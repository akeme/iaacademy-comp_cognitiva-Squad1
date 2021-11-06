from src.gen_function import contadorDeStrigs
import argparse


def main():
    ap = argparse.ArgumentParser()

    ap.add_argument('-lista', '--listaDeStrings',
                    default=['abacate', 'pera', 'pera', 'uva', 'uva', 'feijão', 'arroz']
                    ,
                    help='Lista de strings')

    args = vars(ap.parse_args())

    listStrings = args['listaDeStrings']

    # imprime a quantidade de strings
    print(contadorDeStrigs(listStrings))


if __name__ == '__main__':
    main()
