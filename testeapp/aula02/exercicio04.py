
from src.gen_function import repeticao_string
import argparse

def main():
    '''
    questao 04
    '''

    lista =  "How many fruits do you have in your fruit basket? fruits"

    ap = argparse.ArgumentParser()
    ap.add_argument('-l1', '--lista_de_string',
                    default=lista.split(' '),
                    help='lista de string')

    ap.add_argument('-l2', '--string_a_ser_pesquisada',
                    default="fruits",
                    help='string_a_ser_pesquisada')

    args = vars(ap.parse_args())
    lista = args['lista_de_string']
    sub_string = args['string_a_ser_pesquisada']

    print(repeticao_string(lista,sub_string))


if __name__ == '__main__':
    main()

