# Imports
import Protests_Functions as pf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Functions
# Input should be... one string ..
def count_givenKeyword(text, keywords):
    matched = []
    for word in text:
        if word in keywords:
            matched.append(word)
    return len(matched)


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

GF_keywords = [ 'floyd']
BT_keywords = ['taylor']

# Action
farleft_textP = pf.open_file(farleft_file)
print(type(farleft_textP))
print(len(farleft_textP))
print(farleft_textP[0])

left_textP = pf.open_file(left_file)
center_textP = pf.open_file(center_file)
right_textP = pf.open_file(right_file)
farright_textP = pf.open_file(farright_file)

all_textP = farleft_textP + left_textP + center_textP + right_textP + farright_textP
print(type(all_textP))
print(len(all_textP))
print(all_textP[0])

farleft_textGF = pf.open_file(farleft_fileG)
left_textGF = pf.open_file(left_fileG)
center_textGF = pf.open_file(center_fileG)
right_textGF = pf.open_file(right_fileG)
farright_textGF = pf.open_file(farright_fileG)
all_textGF = farleft_textGF + left_textGF + center_textGF + right_textGF + farright_textGF

farleft_textBT = pf.open_file(farleft_fileB)
left_textBT = pf.open_file(left_fileB)
center_textBT = pf.open_file(center_fileB)
right_textBT = pf.open_file(right_fileB)
farright_textBT = pf.open_file(farright_fileB)
all_textBT = farleft_textBT + left_textBT + center_textBT + right_textBT + farright_textBT

floyd_countGF = count_givenKeyword(all_textGF, GF_keywords)
floyd_countBT = count_givenKeyword(all_textBT, GF_keywords)
floyd_countP = count_givenKeyword(all_textP, GF_keywords)

print('Floyd Floyd:', floyd_countGF)
print('Floyd Taylor:', floyd_countBT)
print('Floyd protests:', floyd_countP)

taylor_countGT = count_givenKeyword(all_textGF, BT_keywords)
taylor_countBT = count_givenKeyword(all_textBT, BT_keywords)
taylor_countP = count_givenKeyword(all_textP, BT_keywords)
print('Taylor Floyd:', taylor_countGT)
print('Taylor Taylor:', taylor_countBT)
print('Taylor protests:', taylor_countP)

# # FloydCount_FL = count_givenKeyword(farleft_textP, 'Floyd')
# # FloydCount_L = count_givenKeyword(left_textP, 'Floyd')
# # FloydCount_C = count_givenKeyword(center_textP, 'Floyd')
# # FloydCount_R = count_givenKeyword(right_textP, 'Floyd')
# # FloydCount_FR = count_givenKeyword(farright_textP, 'Floyd')
# #
# # frequency = [FloydCount_FL, FloydCount_L, FloydCount_C, FloydCount_R, FloydCount_FR]
# # leaning = ['Far left', 'Left', 'Center', 'Right', 'Far Right']
# #
# # all_info = [leaning, frequency]
# # df = pd.DataFrame(all_info).transpose()
# # df.columns = ['Political Leaning', 'Frequency']
# #
# # plot = sns.catplot(x='Political Leaning',y='Frequency', data=df, kind='bar')
# # #plot.set_title('Antifa mentions by newspapers from across the political spectrum covering the BLM protests')
# # plt.show()
