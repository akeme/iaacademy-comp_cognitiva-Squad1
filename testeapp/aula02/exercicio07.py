from src.gen_function import mostrar_duplicados
import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-n1', '--lista', type = list,  default = (1, 2, 3, 3, 'a', 'b', 'c', 'c', 1.1, 1.1, 1.2, 'casa', 'casa', 'carro'), help = 'lista de elementos')

    args = vars(ap.parse_args())

    elementos = args['lista']

    result = mostrar_duplicados(elementos)

    print('Lista de elementos duplicados: ', result)

if __name__ == '__main__':
    main()