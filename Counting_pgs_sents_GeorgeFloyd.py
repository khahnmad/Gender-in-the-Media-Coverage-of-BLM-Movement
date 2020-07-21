import Counting_Paragraphs_and_Sentences as cp


farleft_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/George Floyd - Far Left.csv'
left_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/George Floyd - Left.csv'
center_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/George Floyd - Center.csv'
right_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/George Floyd - Right.csv'
farright_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/George Floyd - Far Right.csv'


farleft_sentences, farleft_words = cp.open_file(farleft_file)
left_sentences, left_words = cp.open_file(left_file)
center_sentences, center_words = cp.open_file(center_file)
right_sentences, right_words = cp.open_file(right_file)
farright_sentences, farright_words = cp.open_file(farright_file)

print('George Floyd')
print('Political leaning', '# of sentences','  # of words')
print('         Far Left', '    ', farleft_sentences,'    ', farleft_words)
print('             Left','    ', left_sentences,'    ', left_words)
print('           Center', '    ',center_sentences,'    ', center_words)
print('            Right','    ',right_sentences,'    ', right_words)
print('        Far Right', '    ',farright_sentences, '    ', farright_words)
