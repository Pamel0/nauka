import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

#prosty
# plt.plot([1, 2, 3, 4, 5])
# plt.ylabel('jakieś liczby')
# plt.show()

#wykres z 2 wektorami
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
# plt.axis([0, 6, 0, 20])
# plt.show()

#wykres z 2 wektorami z pomalowanymi punktami
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
# plt.axis([0, 6, 0, 20])
# plt.show()

#################################################################################################################################################################################
#wykres kołowy plotly
# labels = ['Mirek', 'Jagoda', 'Otylka', 'Elwira', 'Ty :)']
# values = [45, 40, 42, 39, 46]
#
# fig = px.pie(values=values, names=labels,
#              color_discrete_sequence=px.colors.sequential.RdBu)
#
# fig.show()

#wykres kołowy matplotlib
# slices = [8,2,3,13]
# live = ['spanie', 'jedzenie', 'praca', 'zabawa']
# kolor = ['c', 'm', 'r', 'b']
#
# plt.pie(slices, labels = live, colors = kolor,startangle= 90, shadow= True, explode = (0, 0.1, 0, 0), autopct = '%1.1f%%')
#
# plt.title('wykres kołowy \n Sprawdź to!')
# plt.show()


# df = pd.read_csv('automobile.csv', sep=';')
#
# df = df.groupby('Car model').size()
# wedges, texts, autotext = plt.pie(x=df, labels=df.index,
#                                   autopct=lambda pct: "{:.2f}%".format(pct),
# textprops=dict(color='black'))
# plt.title('Auta')
# plt.show()

# df = pd.read_csv('automobile.csv', sep=';')

# lol = df.groupby('Car model').size() #zapamiętać size
# df.tail(n=5)
# wedges, texts, autotext = plt.pie(x=df, labels=df.index,
#                                   autopct=lambda pct: "{:.2f}%".format(pct),
# textprops=dict(color='black'))
# plt.title('Auta')
# plt.show()
# print(df)
###############################################################################################################################################################################
#lasy12
# xlsx = pd.ExcelFile('lasy12.xlsx')
# df = pd.read_excel(xlsx, header=0)
# x = df.Rok
# y = df.Wartość
# t = ("165918")
# plt.text(2020, 1.88, t)
# plt.plot(x, y)
# plt.xlabel('Rok')
# plt.ylabel('Hektary')
# plt.title("Lasy")
# plt.savefig('wykres.png')
# plt.show()


# p = 0.3
# height1 = [6, 35, 1]
# height2 = [7, 27.5, 3]
# y_pos1 = np.arange(len(height1))
# y_pos2 = np.arange(len(height2))
# bars = ('Hipermarkety', 'Supermakety', 'Domy handlowe')
# plt.bar(y_pos1 - p/2, height1, p,  color = 'b', label='Rok 2016')
# plt.bar(y_pos2 + p/2, height2, p,  color = 'orange', label='Rok 2017')
# plt.xticks(y_pos1, bars)
# plt.title('Informacje o sklepach', fontsize=16, color='#323232')
# plt.axis([-0.4,2.5,0,36])
# plt.legend()
# plt.savefig('wykres.pdf')
# plt.show();


csv = pd.read_csv('sklepy12.csv', sep=';')
print(csv)