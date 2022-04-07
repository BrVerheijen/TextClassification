from typing import Dict
from nltk.util import ngrams
import nltk
import csv
from Dataset import GetDataset

FILE = './TextClassification/dataset.csv'

Swedish_Trigram_Total = 0
Dutch_Trigram_Total = 0
French_Trigram_Total = 0
Spanish_Trigram_Total = 0
Romanian_Trigram_Total = 0
English_Trigram_Total = 0

Swedish_Bigram_Total = 0
Dutch_Bigram_Total = 0
French_Bigram_Total = 0
Spanish_Bigram_Total = 0
Romanian_Bigram_Total = 0
English_Bigram_Total = 0

Swedish_Trigrams = {}
Dutch_Trigrams = {}
French_Trigrams = {}
Spanish_Trigrams = {}
Romanian_Trigrams = {}
English_Trigrams = {}

Swedish_Bigrams = {}
Dutch_Bigrams = {}
French_Bigrams = {}
Spanish_Bigrams = {}
Romanian_Bigrams = {}
English_Bigrams = {}

dataset = GetDataset(FILE)

def GetCounts(data):
    for i, j in data.iterrows():
        
        chrs = [c for c in j["Text"]]
        trigrams = list(nltk.trigrams(chrs))
        
        bigrams = list(nltk.bigrams(chrs))
        for trigram in trigrams:
            if j["language"] == "Swedish":
                global Swedish_Trigram_Total
                Swedish_Trigram_Total += 1
                if trigram in Swedish_Trigrams:
                    Swedish_Trigrams[trigram] += 1
                else:
                    Swedish_Trigrams[trigram] = 1

            elif j["language"] == "Dutch":
                global Dutch_Trigram_Total
                Dutch_Trigram_Total += 1
                if trigram in Dutch_Trigrams:
                    Dutch_Trigrams[trigram] += 1
                else:
                    Dutch_Trigrams[trigram] = 1

            elif j["language"] == "French":
                global French_Trigram_Total
                French_Trigram_Total += 1
                if trigram in French_Trigrams:
                    French_Trigrams[trigram] += 1
                else:
                    French_Trigrams[trigram] = 1

            elif j["language"] == "Spanish":
                global Spanish_Trigram_Total
                Spanish_Trigram_Total += 1
                if trigram in Spanish_Trigrams:
                    Spanish_Trigrams[trigram] += 1
                else:
                    Spanish_Trigrams[trigram] = 1

            elif j["language"] == "Romanian":
                global Romanian_Trigram_Total
                Romanian_Trigram_Total += 1
                if trigram in Romanian_Trigrams:
                    Romanian_Trigrams[trigram] += 1
                else:
                    Romanian_Trigrams[trigram] = 1

            elif j["language"] == "English":
                global English_Trigram_Total
                English_Trigram_Total += 1
                if trigram in English_Trigrams:
                    English_Trigrams[trigram] += 1
                else:
                    English_Trigrams[trigram] = 1

            else:
                print("ERROR")

        for bigram in bigrams:
            if j["language"] == "Swedish":
                global Swedish_Bigram_Total
                Swedish_Bigram_Total += 1
                if bigram in Swedish_Bigrams:
                    Swedish_Bigrams[bigram] += 1
                else:
                    Swedish_Bigrams[bigram] = 1

            elif j["language"] == "Dutch":
                global Dutch_Bigram_Total
                Dutch_Bigram_Total += 1
                if bigram in Dutch_Bigrams:
                    Dutch_Bigrams[bigram] += 1
                else:
                    Dutch_Bigrams[bigram] = 1

            elif j["language"] == "French":
                global French_Bigram_Total
                French_Bigram_Total += 1
                if bigram in French_Bigrams:
                    French_Bigrams[bigram] += 1
                else:
                    French_Bigrams[bigram] = 1

            elif j["language"] == "Spanish":
                global Spanish_Bigram_Total
                Spanish_Bigram_Total += 1
                if bigram in Spanish_Bigrams:
                    Spanish_Bigrams[bigram] += 1
                else:
                    Spanish_Bigrams[bigram] = 1

            elif j["language"] == "Romanian":
                global Romanian_Bigram_Total
                Romanian_Bigram_Total += 1
                if bigram in Romanian_Bigrams:
                    Romanian_Bigrams[bigram] += 1
                else:
                    Romanian_Bigrams[bigram] = 1

            elif j["language"] == "English":
                global English_Bigram_Total
                English_Bigram_Total += 1
                if bigram in English_Bigrams:
                    English_Bigrams[bigram] += 1
                else:
                    English_Bigrams[bigram] = 1

            else:
                print("ERROR")

def ChanceEquation(dict, total):
    Ngrams = {}
    for gram in dict:
        Ngrams[gram] = (dict[gram] + 1)/(total + len(dict))
    return Ngrams

def GetEnglishTrigrams():
    GetCounts(dataset)
    Trigrams = ChanceEquation(English_Trigrams, English_Trigram_Total)
    print(Trigrams)

GetEnglishTrigrams()









