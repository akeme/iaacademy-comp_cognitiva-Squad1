from src.gen_function import multiRoi
import argparse
import numpy as np


def main():
    '''
            questao 09
    '''
    ap = argparse.ArgumentParser()
    ap.add_argument('-m', '--mat',
                    default=np.random.rand(5, 5),
                    help='matriz')

    ap.add_argument('-ps', '--pts',
                    default=[[3, 3], [2, 2], [4, 4]],
                    help='pontos centrais das ROIs')

    ap.add_argument('-ts', '--tams',
                    default=[1, 0, 1],
                    help='tamanho das ROIs')

    args = vars(ap.parse_args())
    mat = args['mat']
    pts = args['pts']
    tams = args['tams']
    regis = multiRoi(mat, pts, tams)
    txt = "As ROIs da matrix \n{str1} \nsão \n{str2}"
    print(txt.format(str1=str(mat), str2=str(regis)))


if __name__ == '__main__':
    main()