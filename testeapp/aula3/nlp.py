from src.gen_function import distEucl
import argparse

def main():
    '''
    questao 01
    '''
    ap = argparse.ArgumentParser()
    ap.add_argument('-p1', '--pt1',
                    default=[0, 3],
                    help='primeiro ponto')

    ap.add_argument('-p2', '--pt2',
                    default=[4, 0],
                    help='segundo ponto')

    args = vars(ap.parse_args())
    pt1 = args['pt1']
    pt2 = args['pt2']
    result = distEucl(pt1, pt2)

    txt = "A distância entre {str1} e {str2} é {num:.2f}"
    print(txt.format(str1=str(pt1), str2=str(pt2), num=result))


if __name__ == '__main__':
    main()