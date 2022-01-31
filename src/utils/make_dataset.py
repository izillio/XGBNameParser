import xml.etree.ElementTree as ET
import pandas as pd

def get_XMLtree(path):
    '''Open file, return XML tree root'''
    tree = ET.parse(path)
    root = tree.getroot()
    return root

def exctract_corpus(root):
    ''' Convert XML to corpus in Pandas Series format'''
    corpus = []
    target = []
    for name in root:
        for field in name:
            corpus.append(field.text)
            target.append(field.tag)
    target = pd.Series(target)
    corpus = pd.Series(corpus)
    return corpus, target

def extract_dataset(root):
    ''' Convert XML to tokenized dataset'''
    dataset = []
    targetset = []
    for name in root:
        datapoint = []
        target = []
        for field in name:
            datapoint.append(field.text)
            target.append(field.tag)
        dataset.append(datapoint)
        targetset.append(target)
    return dataset, targetset