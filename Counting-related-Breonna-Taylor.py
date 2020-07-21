# Imports
import Protests_Functions as pf
import csv
from bs4 import BeautifulSoup
import requests
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from cucco import Cucco
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Functions
def open_file(filename):
    # open the file
    csvfile, csvColumns, columnsList, urlsList = [], [], [], []
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
        text = get_page_sentences(url)  # gets stripped p tags from each url
        listsOfSentences.append(text)
    one_list_sentences = []
    for elt in listsOfSentences:  # make it just one list of all the strings
        for i in elt:
            one_list_sentences.append(i)
    return one_list_sentences


def clean_text(one_list_sentences):
    new_stopwords = set(stopwords.words('english'))
    pronouns = ['he', 'his', 'him', 'her', 'hers', 'she']
    for word in pronouns:
        new_stopwords.remove(word)
    all_text, lowered_sentences = [], []
    one_list_sentences = [st.replace("’", "") for st in one_list_sentences]
    one_list_sentences = [st.replace('“', '') for st in one_list_sentences]
    one_list_sentences = [st.replace('”', '') for st in one_list_sentences]
    one_list_sentences = [st.replace('—', '') for st in one_list_sentences]
    print('One list sentences:', type(one_list_sentences), one_list_sentences[0])
    for sentence in one_list_sentences: # make all letters lowercase
        lowered_sentences.append(sentence.lower())
    return lowered_sentences

# Get website text
# input: single url
# output: list of lists which are tokenized sentences
# problems: with the test, has a bunch of empty lists at the end; not clean
def get_page_sentences(url):
    paragraphs_normalized = []
    normEsp = Cucco()
    norms = ['replace_punctuation', 'remove_extra_whitespaces']
    soup = BeautifulSoup(requests.get(url).text, "lxml")
    paragraphs = soup.find_all('p')
    stripped_paragraph = [tag.get_text().strip() for tag in paragraphs]
    for sentence in stripped_paragraph:
        paragraphs_normalized.append(normEsp.normalize(sentence, norms))
    return paragraphs_normalized

# Tokenize
# inputs: list of sentences as strings
# return: list of list of sentences which are tokenized
def get_token_sentences(sentence_list):
    return [word_tokenize(word) for word in sentence_list]

# Search for related words in specific (keyword) sentences
# inputs: list of sentences as a string, list of string of keywords
# Note: sentence_list should NOT be tokenized
# return:  list of related words as strings
def search_related_words(one_list_sentences, keyword_list):
    token_sentences, matched_sentences, related_words_list, lowered_sentences = ([] for i in range(4))
    new_stopwords = set(stopwords.words('english'))
    all_text, lowered_sentences = [], []
    one_list_sentences = [st.replace("’", "") for st in one_list_sentences]
    one_list_sentences = [st.replace('“', '') for st in one_list_sentences]
    one_list_sentences = [st.replace('”', '') for st in one_list_sentences]
    one_list_sentences = [st.replace('—', '') for st in one_list_sentences]
    one_list_sentences = [st.replace('breonna', '') for st in one_list_sentences]
    one_list_sentences = [st.replace('taylors', '') for st in one_list_sentences]
    print('One list sentences:', type(one_list_sentences), one_list_sentences[0])
    # lowercase
    for sentence in one_list_sentences:
        lowered_sentences.append(sentence.lower())
    # token sentences
    token_sentences = get_token_sentences(lowered_sentences)

    # get matched sentences
    for sentence in token_sentences:
        for keyword in keyword_list:
            if (keyword in sentence) and (sentence not in matched_sentences):
                matched_sentences.append(sentence)

    # get related words in matched sentences that are not initial keywords and stopwords
    for sentence in matched_sentences:
        for word in sentence:
            if (word not in new_stopwords) and (word not in keyword_list):
                related_words_list.append(word)
    return related_words_list


def get_BT_relatedwords(farleftfile, leftfile, centerfile, rightfile, farrightfile):
    # Get the text
    farleft_text = open_file(farleftfile)
    left_text = open_file(leftfile)
    center_text = open_file(centerfile)
    right_text = open_file(rightfile)
    farright_text = open_file(farrightfile)
    all_text = farleft_text + left_text + farright_text

    Breonna_related_FL = search_related_words(farleft_text, ['taylor'])
    Breonna_related_L = search_related_words(left_text, ['taylor'])
    Breonna_related_C = search_related_words(center_text, ['taylor'])
    Breonna_related_R = search_related_words(right_text, ['taylor'])
    Breonna_related_FR = search_related_words(farright_text, ['taylor'])
    Breonna_related_AT = search_related_words(all_text, ['taylor'])


    a = pf.plot_freqWords(Breonna_related_FL, 'Breonna Taylor Far left related words')
    b = pf.plot_freqWords(Breonna_related_L, 'Breonna Taylor left related words')
    c = pf.plot_freqWords(Breonna_related_C, 'Breonna Taylor Center related words')
    d = pf.plot_freqWords(Breonna_related_R, 'Breonna Taylor Right related words')
    e = pf.plot_freqWords(Breonna_related_FR, 'Breonna Taylor Far Right related words')
    f = pf.plot_freqWords(Breonna_related_AT, 'Breonna Taylor all related words')


    words, frequency, leaning = [],[],[]
    for word, count in a:
        words.append(word)
        frequency.append(count)
        leaning.append('Far Left')
    for word, count in b:
        words.append(word)
        frequency.append(count)
        leaning.append('Left')
    for word, count in c:
        words.append(word)
        frequency.append(count)
        leaning.append('Center')
    for word, count in d:
        words.append(word)
        frequency.append(count)
        leaning.append('Right')
    for word, count in e:
        words.append(word)
        frequency.append(count)
        leaning.append('Far Right')

    all_info = [words, frequency, leaning]
    df = pd.DataFrame(all_info).transpose()
    df.columns = ['Words', 'Frequency', 'Political Leaning']

    plot = sns.catplot(x='Words',y='Frequency',hue='Political Leaning', data=df, kind='bar')
    # plot.set_title('Frequency of Key Words from Newspapers across the Political Spectrum Covering the Black Lives Matter Protests')
    plt.show()

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

BT_articles = get_BT_relatedwords(farleft_fileB, left_fileB, center_fileB, right_fileB, farright_fileB)
GF_articles = get_BT_relatedwords(farleft_fileG, left_fileG, center_fileG, right_fileG, farright_fileG)
protest_articles = get_BT_relatedwords(farleft_file, left_file, center_file, right_file, farright_file)
