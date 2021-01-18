# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 20:16:06 2020

@author: artur
"""

import random
from matplotlib import pyplot as plt
from collections import Counter


katsed=10000
valikud=["Kivi","Paber","Käärid"]
kogum=[]
for i in range(katsed):
    a=random.choice(valikud)
    kogum.append(a)
loend=Counter(kogum)
uusloend=loend.most_common(3)

x=[]
y=[]
for item in uusloend:
    x.append(item[0])
    y.append(item[1])
    
plt.bar(x, y, edgecolor="black")
plt.tight_layout()
plt.show()