# Imports
import Protests_Functions as pf
import collections
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter


# Functions
def open_file(filename):
    # open the file
    csvfile, csvColumns, columnsList, urlsList, token_sentences, lowered_sentences = [], [], [], [],[], []
    with open(filename, 'r', encoding='utf-8') as f:
        csv_f = csv.reader(f)
        csvfile.append([x for x in csv_f])
    for column in csvfile:
            csvColumns.append(column)
    for elt in csvColumns:  # makes each column a string in one list
        for i in elt:
            columnsList.append(i)
    while '' in columnsList:  # remove empty strings
        columnsList.remove('')
    totalElements = len(columnsList)
    for elt in columnsList:  # remove content that is not a url and remove repeated urls
        for i in elt:
            if i.startswith('http') and i not in urlsList:
                urlsList.append(i)
    totalUnrepeatedElements = len(urlsList)
    listsOfSentences = []
    for url in urlsList:
        text = pf.get_page_sentences(url)  # gets stripped p tags from each url
        listsOfSentences.append(text)
    one_list_sentences = []
    # print('First elemnt of list of Sentences:', listsOfSentences[0])
    # token_sentences = pf.get_token_sentences(listsOfSentences)
    # for sentence in one_list_sentences: # make all letters lowercase
    #     lowered_sentences.append(sentence.lower())
    for elt in listsOfSentences:  # make it just one list of all the strings
        tokenized = pf.get_token_sentences(elt)
        token_sentences.append(tokenized)
    for elt in token_sentences:
        for item in elt:
            one_list_sentences.append(item)
    # one_list_sentences = [st.replace("’", "") for st in one_list_sentences]
    return one_list_sentences

def find_trigrams(text, keyword1, keyword2, keyword3):
    manyNgrams, keywordfirst, matched_ngrams = [], [], []
    for elt in text:
        getNgrams = pf.extract_ngrams(elt, 3)
        manyNgrams.append(getNgrams)
    for elt in manyNgrams:
        for ngram in elt:
            if keyword1 in ngram and keyword2 in ngram and keyword3 in ngram:
                matched_ngrams.append(ngram)
    print('There are ', len(matched_ngrams), 'matched ngrams')
    return matched_ngrams


def find_SHN(farleft_file, left_file, center_file, right_file, farright_file):
    # Open and read file
    FL_text = open_file(farleft_file)
    L_text = open_file(left_file)
    C_text = open_file(center_file)
    R_text = open_file(right_file)
    FR_text = open_file(farright_file)

    # Find trigrams
    SHN_FL = find_trigrams(FL_text, 'say', 'her', 'name')
    SHN_L = find_trigrams(L_text, 'say', 'her', 'name')
    SHN_C = find_trigrams(C_text, 'say', 'her', 'name')
    SHN_R = find_trigrams(R_text, 'say', 'her', 'name')
    SHN_FR = find_trigrams(FR_text, 'say', 'her', 'name')

    print('Far left:', SHN_FL)
    print('Right:', SHN_R)
    return SHN_FL, SHN_L, SHN_C, SHN_R, SHN_FR

# Variables

# Breonna Taylor articles
farleft_fileB = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Breonna Taylor  - Far Left.csv'
left_fileB = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Breonna Taylor  - Left.csv'
center_fileB = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Breonna Taylor  - Center.csv'
right_fileB = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Breonna Taylor  - Right.csv'
farright_fileB = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Breonna Taylor  - Far right.csv'

# George Floyd articles
farleft_fileG = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/George Floyd - Far Left.csv'
left_fileG = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/George Floyd - Left.csv'
center_fileG = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/George Floyd - Center.csv'
right_fileG = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/George Floyd - Right.csv'
farright_fileG = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/George Floyd - Far Right.csv'

# Protests articles
farleft_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Far Left.csv'
left_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Left.csv'
center_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Center.csv'
right_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Right.csv'
farright_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Far Right.csv'

# Action

bt_fl, bt_l, bt_c, bt_r, bt_fr = find_SHN(farleft_fileB, left_fileB, center_fileB, right_fileB, farright_fileB)
gf_fl, gf_l, gf_c, gf_r, gf_fr = find_SHN(farleft_fileG, left_fileG, center_fileG, right_fileG, farright_fileG)
p_fl, p_l, p_c, p_r, p_fr = find_SHN(farleft_file, left_file, center_file, right_file, farright_file,)


