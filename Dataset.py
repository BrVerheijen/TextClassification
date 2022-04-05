import csv
import nltk
import pandas

def GetDataset(FILE):
    dataset = pandas.read_csv(FILE)
    return dataset



