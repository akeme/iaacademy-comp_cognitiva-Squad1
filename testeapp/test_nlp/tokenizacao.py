from src.nlp_proc import tokenizar
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-p1', '--texto', default='Macaco come banana todos os dias, hoje está nublado. amanhã é sexta.')
    ap.add_argument('-p2', '--idioma', default='pt')
    ap.add_argument('-p3', '--quebrar_linha', default=False)
    args = vars(ap.parse_args())

    #stanza.download(idioma)

    result = tokenizar(args['texto'], args['idioma'], args['quebrar_linha'])

    print(result)

if __name__ == '__main__':
    main()
