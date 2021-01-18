# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 21:32:53 2020

@author: artur
"""


import random
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


valikud=["1","2","3","4","5","6"]
tulemused=[]

plt.style.use("fivethirtyeight")

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

x_values=[]
y_values=[]

def animate(i):

    a=random.choice(valikud)
    tulemused.append(a)
    loend=Counter(tulemused)
    saame=loend.most_common(10)

    for values in saame:
        x_values.append(values[0])
        y_values.append(values[1])
    
    ax1.clear()
    ax1.bar(x_values,y_values)
 
ani =FuncAnimation(plt.gcf(), animate, interval= 1)
    
plt.tight_layout()
plt.show()