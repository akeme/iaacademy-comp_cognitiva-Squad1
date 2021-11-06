from src.gen_function import limiar_array
import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-n1', '--matriz', type = list,  default = [[ 1.,  2.,  3.,  4.],
                                                               [ 1.,  2.,  3.,  4.],
                                                               [ 1.,  2.,  3.,  4.],
                                                               [ 1.,  2.,  3.,  4.]], help = 'Matriz')
    ap.add_argument('-n2', '--limiar', type=list, default=  3, help='Limiar')

    args = vars(ap.parse_args())

    matriz = args['matriz']
    limiar = args['limiar']

    result = limiar_array(matriz, limiar)

    print('Matriz binarizada: ', result)

if __name__ == '__main__':
    main()