# Import
import Protests_Functions as pf
import collections
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter


# Functions

# gets ngrams from a text that start with a given keyword
# input: clean, tokenized list of lists of strings; the keyword; the size of the ngram
# output: prints the 5 most common ngrams, returns uncounted ngrams
def load_ngrams_onekeywordfirst(text, keyword, number):
    manyNgrams, keywordfirst = [], []
    for elt in text:
        getNgrams = pf.extract_ngrams(elt, number)
        manyNgrams.append(getNgrams)
    for i in manyNgrams:
        for gram in i:
            # if gram.startswith(keyword): #and (gram not in keywordfirst):
            if keyword in gram:
                keywordfirst.append(gram)
    keywordfirstFreq = collections.Counter(keywordfirst)
    print(keywordfirstFreq.most_common(10))
    return keywordfirstFreq.most_common(10)


def open_file(filename):
    # open the file
    csvfile, csvColumns, columnsList, urlsList, token_sentences = [], [], [], [],[]
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
    for elt in listsOfSentences:  # make it just one list of all the strings
        tokenized = pf.get_token_sentences(elt)
        token_sentences.append(tokenized)
    for elt in token_sentences:
        for item in elt:
            one_list_sentences.append(item)
    # one_list_sentences = [st.replace("’", "") for st in one_list_sentences]
    return one_list_sentences


# def plot_ngrams(ngram_list, title):
#     counter = Counter(ngramt_list)
#     most = counter.most_common()
#     x, y = [], []
#     for ngram, count in ngram_list:
#         x.append(ngram)
#         y.append(count)
#     sns.barplot(x=y, y=x, color='cyan').set_title(title)
#     plt.show()


def plot_allNgrams(farleft, left, center, right, farright):
    words, frequency, leaning = [], [], []
    for word, count in farleft:
        words.append(word)
        frequency.append(count)
        leaning.append('Far Left')
    for word, count in left:
        words.append(word)
        frequency.append(count)
        leaning.append('Left')
    for word, count in center:
        words.append(word)
        frequency.append(count)
        leaning.append('Center')
    for word, count in right:
        words.append(word)
        frequency.append(count)
        leaning.append('Right')
    for word, count in farright:
        words.append(word)
        frequency.append(count)
        leaning.append('Far Right')

    all_info = [words, frequency, leaning]
    df = pd.DataFrame(all_info).transpose()
    df.columns = ['Words', 'Frequency', 'Political Leaning']

    plot = sns.catplot(x='Words', y='Frequency', hue='Political Leaning', data=df, kind='bar')
    # plot.set_title('Frequency of Key Words from Newspapers across the Political Spectrum Covering the Black Lives Matter Protests')
    plt.show()


def find_specificNgrams(text, number, keyword1, keyword2):
    manyNgrams, keywordfirst = [], []
    for elt in text:
        getNgrams = pf.extract_ngrams(elt, number)
        manyNgrams.append(getNgrams)
    matched_ngrams =[]
    for elt in manyNgrams:
        for ngram in elt:
            if keyword1 in ngram and keyword2 in ngram:
                matched_ngrams.append(ngram)
    print('There are ', len(matched_ngrams), 'matched ngrams')
    counter = Counter(matched_ngrams)
    most = counter.most_common()
    print(most[:10])
    return matched_ngrams


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


farleft_textG = open_file(farleft_fileG)
left_textG = open_file(left_fileG)
center_textG = open_file(center_fileG)
right_textG = open_file(right_fileG)
farright_textG = open_file(farright_fileG)
all_textG = farleft_textG + left_textG + center_textG + right_textG + farright_textG
print('Got the G files')

farleft_textB = open_file(farleft_fileB)
left_textB = open_file(left_fileB)
center_textB = open_file(center_fileB)
right_textB = open_file(right_fileB)
farright_textB = open_file(farright_fileB)
all_textB = farleft_textB + left_textB + center_textB + right_textB + farright_textB
print('Got the B files')

farleft_textP = open_file(farleft_file)
left_textP = open_file(left_file)
center_textP = open_file(center_file)
right_textP = open_file(right_file)
farright_textP = open_file(farright_file)
all_textP = farleft_textP + left_textP + center_textP + right_textP + farright_textP
print('Got the P files')

all_text = all_textB + all_textG + all_textP

all_farleft = farleft_textP + farleft_textB + farleft_textG
all_left = left_textP + left_textB + left_textG
all_center = center_textP + center_textB + center_textG
all_right = right_textP + right_textB + right_textG
all_farright = farright_textP + farright_textB + farright_textG

# farleft_ngrams = load_ngrams_onekeywordfirst(all_farleft, 'Floyd ', 5)
# left_ngrams = load_ngrams_onekeywordfirst(all_left, 'Floyd ', 5)
# center_ngrams = load_ngrams_onekeywordfirst(all_center, 'Floyd ', 5)
# right_ngrams = load_ngrams_onekeywordfirst(all_right, 'Floyd ', 5)
# farright_ngrams = load_ngrams_onekeywordfirst(all_farright, 'Floyd ', 5)
#
# farleft_ngrams1 = load_ngrams_onekeywordfirst(all_farleft, 'Taylor ', 5)
# left_ngrams1 = load_ngrams_onekeywordfirst(all_left, 'Taylor ', 5)
# center_ngrams1 = load_ngrams_onekeywordfirst(all_center, 'Taylor ', 5)
# right_ngrams1 = load_ngrams_onekeywordfirst(all_right, 'Taylor ', 5)
# farright_ngrams1 = load_ngrams_onekeywordfirst(all_farright, 'Taylor ', 5)

# all_ngramsG = load_ngrams_onekeywordfirst(all_textG, 'George ', 5)
# all_ngramsB = load_ngrams_onekeywordfirst(all_textB, 'George ', 5)
# all_ngramsP = load_ngrams_onekeywordfirst(all_textP, 'George ', 5)

# plot_allNgrams(farleft_ngrams, left_ngrams, center_ngrams, right_ngrams, farright_ngrams)
# plot_allNgrams(farleft_ngrams1, left_ngrams1, center_ngrams1, right_ngrams1, farright_ngrams1)


familyBT_ngramsFL = find_specificNgrams(farleft_textB, 5, 'Taylor ', 'family')
familyBT_ngramsL = find_specificNgrams(left_textB, 5, 'Taylor ', 'family')
familyBT_ngramsC = find_specificNgrams(center_textB, 5, 'Taylor ', 'family')
familyBT_ngramsR = find_specificNgrams(right_textB, 5, 'Taylor ', 'family')
familyBT_ngramsFR = find_specificNgrams(farright_textB, 5, 'Taylor ', 'family')

familyGF_ngramsFL = find_specificNgrams(farleft_textG, 5, 'Floyd ', 'family')
familyGF_ngramsL = find_specificNgrams(left_textG, 5, 'Floyd ', 'family')
familyGF_ngramsC = find_specificNgrams(center_textG, 5, 'Floyd ', 'family')
familyGF_ngramsR = find_specificNgrams(right_textG, 5, 'Floyd ', 'family')
familyGF_ngramsFR = find_specificNgrams(farright_textG, 5, 'Floyd ', 'family')

boyfriendBT_ngramsFL = find_specificNgrams(farleft_textB, 5, 'Taylor ', 'boyfriend')
boyfriendBT_ngramsL = find_specificNgrams(left_textB, 5, 'Taylor ', 'boyfriend')
boyfriendBT_ngramsC = find_specificNgrams(center_textB, 5, 'Taylor ', 'boyfriend')
boyfriendBT_ngramsR = find_specificNgrams(right_textB, 5, 'Taylor ', 'boyfriend')
boyfriendBT_ngramsFR = find_specificNgrams(farright_textB, 5, 'Taylor ', 'boyfriend')

girlfriendGF_ngramsFL = find_specificNgrams(farleft_textG, 5, 'Floyd ', 'girlfriend')
girlfriendGF_ngramsL = find_specificNgrams(left_textG, 5, 'Floyd ', 'girlfriend')
girlfriendGF_ngramsC = find_specificNgrams(center_textG, 5, 'Floyd ', 'girlfriend')
girlfriendGF_ngramsR = find_specificNgrams(right_textG, 5, 'Floyd ', 'girlfriend')
girlfriendGF_ngramsFR = find_specificNgrams(farright_textG, 5, 'Floyd ', 'girlfriend')

murderBT_ngramsFL = find_specificNgrams(farleft_textB, 5, 'Taylor ', 'murder')
murderBT_ngramsL = find_specificNgrams(left_textB, 5, 'Taylor ', 'murder')
murderBT_ngramsC = find_specificNgrams(center_textB, 5, 'Taylor ', 'murder')
murderBT_ngramsR = find_specificNgrams(right_textB, 5, 'Taylor ', 'murder')
murderBT_ngramsFR = find_specificNgrams(farright_textB, 5, 'Taylor ', 'murder')

murderGF_ngramsFL = find_specificNgrams(farleft_textG, 5, 'Floyd ', 'murder')
murderGF_ngramsL = find_specificNgrams(left_textG, 5, 'Floyd ', 'murder')
murderGF_ngramsC = find_specificNgrams(center_textG, 5, 'Floyd ', 'murder')
murderGF_ngramsR = find_specificNgrams(right_textG, 5, 'Floyd ', 'murder')
murderGF_ngramsFR = find_specificNgrams(farright_textG, 5, 'Floyd ', 'murder')

deathBT_ngramsFL = find_specificNgrams(farleft_textB, 5, 'Taylor ', 'death')
deathBT_ngramsL = find_specificNgrams(left_textB, 5, 'Taylor ', 'death')
deathBT_ngramsC = find_specificNgrams(center_textB, 5, 'Taylor ', 'death')
deathBT_ngramsR = find_specificNgrams(right_textB, 5, 'Taylor ', 'death')
deathBT_ngramsFR = find_specificNgrams(farright_textB, 5, 'Taylor ', 'death')

deathGF_ngramsFL = find_specificNgrams(farleft_textG, 5, 'Floyd ', 'death')
deathGF_ngramsL = find_specificNgrams(left_textG, 5, 'Floyd ', 'death')
deathGF_ngramsC = find_specificNgrams(center_textG, 5, 'Floyd ', 'death')
deathGF_ngramsR = find_specificNgrams(right_textG, 5, 'Floyd ', 'death')
deathGF_ngramsFR = find_specificNgrams(farright_textG, 5, 'Floyd ', 'death')

drugsBT_ngrams = find_specificNgrams(all_text, 5, 'Taylor ', 'drugs')
drugsGF_ngrams = find_specificNgrams(all_text, 5, 'Floyd ', 'drugs')
