import pandas as pd
import spacy
import numpy as np


USUARIO = { 'JB' : 0}

#SPACY = spacy.load('pt_core_news_sm')

dataset = pd.read_csv('jairbolsonaro.csv')

#ataset.iloc["usuario"] = dataset.iloc["usuario"].aplly(lambda x: USUARIO[x])

comprimento_frases = np.fromiter((len(t.split()) for t in dataset["usuario"]), count=len(dataset["usuario"]), dtype='uint32')

print('Tamanho minimo da frase {}: "{}"'.format(np.min(comprimento_frases),dataset["texto"][np.argmin(comprimento_frases)]))

