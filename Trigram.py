from nltk.util import ngrams
import nltk
import csv
from Dataset import GetDataset

FILE = './TextClassification/dataset.csv'

Estonian_Total = 0
Swedish_Total = 0
Thai_Total = 0
Tamil_Total = 0
Dutch_Total = 0
Japanese_Total = 0
Turkish_Total = 0
Latin_Total = 0
Urdu_Total = 0
Indonesian_Total = 0
Portugese_Total = 0
French_Total = 0
Chinese_Total = 0
Korean_Total = 0
Hindi_Total = 0
Spanish_Total = 0
Pushto_Total = 0
Persian_Total = 0
Romanian_Total = 0
Russian_Total = 0
English_Total = 0
Arabic_Total = 0

Estonian_Trigrams = {}
Swedish_Trigrams = {}
Thai_Trigrams = {}
Tamil_Trigrams = {}
Dutch_Trigrams = {}
Japanese_Trigrams = {}
Turkish_Trigrams = {}
Latin_Trigrams = {}
Urdu_Trigrams = {}
Indonesian_Trigrams = {}
Portugese_Trigrams = {}
French_Trigrams = {}
Chinese_Trigrams = {}
Korean_Trigrams = {}
Hindi_Trigrams = {}
Spanish_Trigrams = {}
Pushto_Trigrams = {}
Persian_Trigrams = {}
Romanian_Trigrams = {}
Russian_Trigrams = {}
English_Trigrams = {}
Arabic_Trigrams = {}


bigram = []
trigram = []

data = GetDataset(FILE)



for i, j in data.iterrows():
    
    text = j["Text"].split()
    trigrams = list(nltk.trigrams(text))
    bigrams = list(nltk.bigrams(text))

    for trigram in trigrams:
        if j["language"] == "Estonian":
            Estonian_Total += 1
            if trigram in Estonian_Trigrams:
                Estonian_Trigrams[trigram] += 1
            else:
                Estonian_Trigrams[trigram] = 1

        if j["language"] == "Swedish":
            Swedish_Total += 1
            if trigram in Swedish_Trigrams:
                Swedish_Trigrams[trigram] += 1
            else:
                Swedish_Trigrams[trigram] = 1

        if j["language"] == "Thai":
            Thai_Total += 1
            if trigram in Thai_Trigrams:
                Thai_Trigrams[trigram] += 1
            else:
                Thai_Trigrams[trigram] = 1

        if j["language"] == "Tamil":
            Tamil_Total += 1
            if trigram in Tamil_Trigrams:
                Tamil_Trigrams[trigram] += 1
            else:
                Tamil_Trigrams[trigram] = 1
                
        if j["language"] == "Dutch":
            Dutch_Total += 1
            if trigram in Dutch_Trigrams:
                Dutch_Trigrams[trigram] += 1
            else:
                Dutch_Trigrams[trigram] = 1

        if j["language"] == "Japanese":
            Japanese_Total += 1
            if trigram in Japanese_Trigrams:
                Japanese_Trigrams[trigram] += 1
            else:
                Japanese_Trigrams[trigram] = 1

        if j["language"] == "Turkish":
            Turkish_Total += 1
            if trigram in Turkish_Trigrams:
                Turkish_Trigrams[trigram] += 1
            else:
                Turkish_Trigrams[trigram] = 1

        if j["language"] == "Latin":
            Latin_Total += 1
            if trigram in Latin_Trigrams:
                Latin_Trigrams[trigram] += 1
            else:
                Latin_Trigrams[trigram] = 1

        if j["language"] == "Urdu":
            Urdu_Total += 1
            if trigram in Urdu_Trigrams:
                Urdu_Trigrams[trigram] += 1
            else:
                Urdu_Trigrams[trigram] = 1

        if j["language"] == "Indonesian":
            Indonesian_Total += 1
            if trigram in Indonesian_Trigrams:
                Indonesian_Trigrams[trigram] += 1
            else:
                Indonesian_Trigrams[trigram] = 1

        if j["language"] == "Portugese":
            Portugese_Total += 1
            if trigram in Portugese_Trigrams:
                Portugese_Trigrams[trigram] += 1
            else:
                Portugese_Trigrams[trigram] = 1

        if j["language"] == "French":
            French_Total += 1
            if trigram in French_Trigrams:
                French_Trigrams[trigram] += 1
            else:
                French_Trigrams[trigram] = 1

        if j["language"] == "Chinese":
            Chinese_Total += 1
            if trigram in Chinese_Trigrams:
                Chinese_Trigrams[trigram] += 1
            else:
                Chinese_Trigrams[trigram] = 1

        if j["language"] == "Korean":
            Korean_Total += 1
            if trigram in Korean_Trigrams:
                Korean_Trigrams[trigram] += 1
            else:
                Korean_Trigrams[trigram] = 1

        if j["language"] == "Hindi":
            Hindi_Total += 1
            if trigram in Hindi_Trigrams:
                Hindi_Trigrams[trigram] += 1
            else:
                Hindi_Trigrams[trigram] = 1

        if j["language"] == "Spanish":
            Spanish_Total += 1
            if trigram in Spanish_Trigrams:
                Spanish_Trigrams[trigram] += 1
            else:
                Spanish_Trigrams[trigram] = 1

        if j["language"] == "Pushto":
            Pushto_Total += 1
            if trigram in Pushto_Trigrams:
                Pushto_Trigrams[trigram] += 1
            else:
                Pushto_Trigrams[trigram] = 1

        if j["language"] == "Persian":
            Persian_Total += 1
            if trigram in Persian_Trigrams:
                Persian_Trigrams[trigram] += 1
            else:
                Persian_Trigrams[trigram] = 1

        if j["language"] == "Romanian":
            Romanian_Total += 1
            if trigram in Romanian_Trigrams:
                Romanian_Trigrams[trigram] += 1
            else:
                Romanian_Trigrams[trigram] = 1

        if j["language"] == "Russian":
            Russian_Total += 1
            if trigram in Russian_Trigrams:
                Russian_Trigrams[trigram] += 1
            else:
                Russian_Trigrams[trigram] = 1

        if j["language"] == "English":
            English_Total += 1
            if trigram in English_Trigrams:
                English_Trigrams[trigram] += 1
            else:
                English_Trigrams[trigram] = 1

        if j["language"] == "Arabic":
            Arabic_Total += 1
            if trigram in Arabic_Trigrams:
                Arabic_Trigrams[trigram] += 1
            else:
                Arabic_Trigrams[trigram] = 1

        else: 
            continue



print(English_Trigrams)
print(English_Total)            

#dictionary voor Estonian, Swedish, Thai, Tamil, Dutch, Japanese, Turkish, Latin, Urdu, Indonesian, Portugese, French, Chinese, Korean, Hindi, Spanish, Pushto, Persian, Romanian, Russian, English, Arabic


