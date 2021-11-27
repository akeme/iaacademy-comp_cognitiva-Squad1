from src.nlp_proc import stop_words
import argparse
import nltk
import string

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-p1', '--tokens', default=['macaco', 'come', 'banana', 'todos', 'os', 'dias', ',', 'hoje', 'está', 'nublado', '.'])
    ap.add_argument('-p2', '--lista_stop_words', default=nltk.corpus.stopwords.words('portuguese'))
    ap.add_argument('-p3', '--pontuacao', default=string.punctuation)
    args = vars(ap.parse_args())

    # nltk.download('stopwords')

    result = stop_words(args['tokens'], args['lista_stop_words'], args['pontuacao'])

    print(result)

if __name__ == '__main__':
    main()
