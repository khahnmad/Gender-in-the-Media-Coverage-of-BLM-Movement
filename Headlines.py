import Protests_Functions as pf
import csv

farleft_fileB = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Breonna Taylor  - Far Left.csv'
left_fileB = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Breonna Taylor  - Left.csv'
center_fileB = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Breonna Taylor  - Center.csv'
right_fileB = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Breonna Taylor  - Right.csv'
farright_fileB = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Breonna Taylor  - Far right.csv'


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
            if i.startswith('http'):
                urlsList.append(i)
    totalUnrepeatedElements = len(urlsList)
    listsOfSentences = []
    print(urlsList)
    for url in urlsList:
        text = pf.get_page_h1(url)  # gets stripped p tags from each url
        listsOfSentences.append(text)
    # one_list_sentences = []
    # for elt in listsOfSentences:  # make it just one list of all the strings
    #     for i in elt:
    #         one_list_sentences.append(i)
    # all_text = clean_text(one_list_sentences)
    return listsOfSentences

farleft_headlines = open_file(farleft_fileB)
print('Far Left:')
print(farleft_headlines)
left_headlines = open_file(left_fileB)
print('Left:')
print(left_headlines)
center_headlines = open_file(center_fileB)
print('Center:')
print(center_headlines)
right_headlines = open_file(right_fileB)
print('Right:')
print(right_headlines)
farright_headlines = open_file(farright_fileB)
print('Far Right:')
print(farright_headlines)
