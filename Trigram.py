from nltk.util import ngrams
import nltk
import csv
from Dataset import GetDataset

FILE = './TextClassification/dataset.csv'

bigram = []
trigram = []

data = GetDataset(FILE)

for row in data.index:
    print(data["Text"][row], data["Language"][row])


