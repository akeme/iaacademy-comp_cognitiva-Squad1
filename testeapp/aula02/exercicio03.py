from src.gen_function import ordenalista
import argparse
import numpy as np

def main():
    ap = argparse.ArgumentParser()

    ap.add_argument('-lista', '--listadeentrada',
                    default=np.array(['Banana', 'Manga', 'Goiaba', 'Laranja', 'Uva', 'Abacate', 'Uva', 'Pera', 'Pizza']),
                    help='Lista a ser ordenada')
    ap.add_argument('-ordena', '--ordenar',
                    default=False,
                    help='valor booleano')

    args = vars(ap.parse_args())

    listafrutas = args['listadeentrada']
    ordenar = args['ordenar']

    print(ordenalista(listafrutas, ordenar))

if __name__ == '__main__':
    main()
