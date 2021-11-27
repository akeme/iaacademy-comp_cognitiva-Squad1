from src.nlp_proc import pre_processamento
import argparse
import nltk
import string

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-p1', '--paginas', default=['Macaco come banana todos os dias, hoje está nublado. amanhã é sexta.','graças a Deus hoje é sexta e estou muito cansado de esperar o final de semana'])
    ap.add_argument('-p2', '--idioma', default='pt')
    ap.add_argument('-p3', '--quebrar_linha', default=False)
    ap.add_argument('-p4', '--lista_stop_words', default=nltk.corpus.stopwords.words('portuguese'))
    ap.add_argument('-p5', '--pontuacao', default=string.punctuation)
    args = vars(ap.parse_args())

    # nltk.download('stopwords')

    result = pre_processamento(args['paginas'], args['idioma'], args['quebrar_linha'], args['lista_stop_words'], args['pontuacao'])

    print(result)

if __name__ == '__main__':
    main()