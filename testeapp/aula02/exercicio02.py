from src.gen_function import maisProx
import argparse

def main():
    '''
    questao 02
    '''
    ap = argparse.ArgumentParser()
    ap.add_argument('-p', '--pt',
                    default=[0, 3],
                    help='primeiro ponto')

    ap.add_argument('-l', '--lp',
                    default=[[4, 0], [10, 30], [0, 3.4]],
                    help='Lista de pontos')

    args = vars(ap.parse_args())
    pt = args['pt']
    lp = args['lp']
    prox = maisProx(pt, lp)
    txt = "O ponto mais próximo de {str1} é {str2}"
    print(txt.format(str1=str(pt), str2=str(prox)))


if __name__ == '__main__':
    main()