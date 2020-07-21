import Counting_Paragraphs_and_Sentences as cp


farleft_fileB = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Breonna Taylor  - Far Left.csv'
left_fileB = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Breonna Taylor  - Left.csv'
center_fileB = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Breonna Taylor  - Center.csv'
right_fileB = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Breonna Taylor  - Right.csv'
farright_fileB = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Breonna Taylor  - Far right.csv'


farleft_sentencesB, farleft_wordsB = cp.open_file(farleft_fileB)
left_sentencesB, left_wordsB = cp.open_file(left_fileB)
center_sentencesB, center_wordsB = cp.open_file(center_fileB)
right_sentencesB, right_wordsB = cp.open_file(right_fileB)
farright_sentencesB, farright_wordsB = cp.open_file(farright_fileB)

print('Breonna Taylor')
print('Political leaning', '# of sentences','  # of words')
print('         Far Left', '    ', farleft_sentencesB,'    ', farleft_wordsB)
print('             Left','    ', left_sentencesB,'    ', left_wordsB)
print('           Center', '    ',center_sentencesB,'    ', center_wordsB)
print('            Right','    ',right_sentencesB,'    ', right_wordsB)
print('        Far Right', '    ',farright_sentencesB, '    ', farright_wordsB)
