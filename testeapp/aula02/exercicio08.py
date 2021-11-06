from src.gen_function import roi
import argparse
import numpy as np


def main():
    '''
        questao 08
    '''
    ap = argparse.ArgumentParser()
    ap.add_argument('-m', '--mat',
                    default=np.random.rand(6, 6),
                    help='matriz')

    ap.add_argument('-p', '--pt',
                    default=[1, 2],
                    help='ponto central da ROI')

    ap.add_argument('-t', '--tam',
                    default=1,
                    help='tamanho da ROI')

    args = vars(ap.parse_args())
    mat = args['mat']
    pt = args['pt']
    tam = args['tam']
    regi = roi(mat, pt, tam)
    txt = "A ROI da matrix \n{str1} \né \n{str2}"
    print(txt.format(str1=str(mat), str2=str(regi)))


if __name__ == '__main__':
    main()