# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:51:18 2020

@author: artur
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import random

plt.style.use("seaborn")

sigma = 0.1 #standardhälve delta Theta jaoks, mis allub normaal jaotusele.
alpha = 30 # alfa Beeta jaotuse jaoks
beeta= 30 # beta Beeta jaotuse jaoks
katsed_n = 100 # n
x = 35  # katsete õnnestumiste hulk X

iteratsioonid=10000
def q(teeta): 
    return (teeta**(alpha-1))*((1-teeta)**(beeta-1)) 

def binoom(teeta):
    return ((math.factorial(katsed_n)/(math.factorial(x)*math.factorial(katsed_n-x)))*((teeta**(x))*(1-teeta)**(katsed_n-x)))

def metropolis(iteratsioonid):
    teeta = 0.1 #
    x=0
    x_list=[]
    pts=[] # parameetri teeta suurused lähevad siia
    vastuvõtmiste_arv=0
    for i in range(iteratsioonid):
        x+=1
        x_list.append(x) # trace-ploti jaoks.
        
        uus_teeta=teeta+np.random.normal(0, sigma)
        ratio= (binoom(uus_teeta)*q(uus_teeta))/(binoom(teeta)*q(teeta))
        acceptance=min(1, ratio)
        U=random.uniform(0,1)
        
        if U < acceptance: 
            teeta=uus_teeta
            vastuvõtmiste_arv+=1
        else:
            teeta=teeta
        pts.append(teeta)
        
    pts=np.array(pts)
    x_list=np.array(x_list)
    
    
    return x_list, pts, vastuvõtmiste_arv

tulemus=metropolis(iteratsioonid)

fig, axs = plt.subplots(1, 2)
axs[0].invert_xaxis()
axs[1].plot(tulemus[0], tulemus[1])
axs[1].set_xlabel('Iteratsioonid',fontsize=12)
axs[1].set_title('Metropolis-Hastings \u03B8-le ', fontsize=18)
axs[1].set_ylabel('Parameeter: \u03B8',fontsize=12)

axs[0].hist(tulemus[1], bins=250, orientation="horizontal") # orientation="horizontal" kui soovid graafikut ümber lükkata

axs[0].set_title('Parameetri \u03B8 jaotus', fontsize=18)

plt.show()

vastuvõttu_määr=tulemus[2]/iteratsioonid
print("Vastuvõttu määr on: " + str(vastuvõttu_määr*100)+"%")
        