# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:23:54 2020

@author: artur
"""

from collections import Counter
from matplotlib import pyplot as plt
with open(r"C:\Users\artur\Desktop\Minu tööd\File handling\tekstid\faust eng.txt", "r", encoding='utf-8') as infile: # ,open(r"C:\Users\artur\Desktop\Uuendus.txt", "w") as outfile:
    data=infile.read()
    data=data.replace(".", "")
    data=data.replace(",", "")
    data=data.replace("/","")
    data=data.replace("?","")
    data=data.replace('“','')
    data=data.replace('„','')
    data=data.replace('\n',' ')
    data=data.replace("'","")
    data=data.replace('–','')
    sõna_kaupa=data.split(" ") # Laome kõik sõnad iga tühiku tagant listi.
    uus=[sõna.lower() for sõna in sõna_kaupa] #list comprehension. ".split()" oli meil juba kõik sõnad listi pannud, aga nüüd asendame kõik suured algustähed väikestega.
    
    
    
tulemused=Counter(uus)     # Loendame nimekirja kõikide sõnadega. (koostab sõnaraamatu kujul [( sõna : kogus)] )
graafiku_andmed=tulemused.most_common(100) # Kuna Counter on veidrat tüüpi, siis kasutan most_common funktsiooni, et teisendada see Dict tüübiks.
# print(graafiku_andmed)
x=[]
y=[]

for i in graafiku_andmed:
    x.append(i[0])
    y.append(i[1])

plt.bar(x, y, edgecolor="black")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()