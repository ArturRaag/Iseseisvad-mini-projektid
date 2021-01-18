# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 20:33:05 2020

@author: artur
"""

import random
from matplotlib import pyplot as plt

# Koostame sündmuste jaotus graafikud. Kasuta selle jaoks matplotlib libraryt.
katsed= 10
tulemused=[]
   
for i in range(katsed):
    a=random.randint(1,6) # Täringut veeretades random tulemus.
    tulemused.append(a) #Lisame järjest tulemused listi.
# print(tulemused)
plt.hist(x=tulemused, bins=[1,2,3,4,5,6,7], edgecolor="black")
plt.tight_layout()
plt.show()