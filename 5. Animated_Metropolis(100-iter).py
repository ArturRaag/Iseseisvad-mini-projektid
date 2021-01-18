# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:18:35 2020

@author: artur
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import random


"""   METROPOLIS-HASTINGS ALGORITHM   """

sigma = 0.1 #standardhälve delta Theta jaoks, mis allub normaaljaotusele.
alpha = 30 # alfa Beeta jaotuse jaoks
beeta= 30 # beta Beeta jaotuse jaoks
katsed_n = 10 # n
x_õnnestumine = 4 # katsete õnnestumiste hulk X

iteratsioonid=200

fig, axs = plt.subplots(1, 2)
plt.style.use('seaborn-bright')

def q(teeta): # ettepanekutuum
    return (teeta**(alpha-1))*((1-teeta)**(beeta-1)) 

def binoom(teeta):
    return ((math.factorial(katsed_n)/(math.factorial(x_õnnestumine)
    *math.factorial(katsed_n-x_õnnestumine)))*((teeta**(x_õnnestumine))*(1-teeta)**(katsed_n-x_õnnestumine)))

teeta = 0.01 # Kuna 0 ja 1 annavad nimetajasse nulli, siis alustame 2-st
samm=0
x_list=[]
pts=[] # parameetri teeta suurused lähevad siia
vastuvõtmiste_arv=0


for i in range(iteratsioonid):
    
    x_list.append(samm) # trace-ploti jaoks.
    uus_teeta=teeta+np.random.normal(0, sigma)
    ratio= (binoom(uus_teeta)*q(uus_teeta))/(binoom(teeta)*q(teeta))
    acceptance=min(1.00, ratio)
    U=random.uniform(0,1) 
    if U < acceptance: 
        teeta=uus_teeta
        marker_värv="green"
        vastuvõtmiste_arv+=1
        graafiku_text=("Võtame vastu uue parameetri \u03B8.")
        graafiku_text_2=("Iteratsioon = "+str(i+1)+"\n\u03B1= "+str(round(acceptance,2))+">"+"U="+str(round(U,2))+"~ U(0,1)")
        acceptance_text=(" ")
    else: # Reject
        teeta=teeta
        marker_värv="red"
        graafiku_text="Keeldume võtmast vastu uut parameetrit \u03B8."
        graafiku_text_2=("Iteratsioon = "+str(i+1)+"\n\u03B1= "+str(round(acceptance,2))+"<"+"U="+str(round(U,2))+"~ U(0,1)")
        
    
    pts.append(teeta)
    
    vastuvõttu_määr=round(vastuvõtmiste_arv/(i+1),2)
    vvm_text="Vastuvõttu määr on: " + str(round(vastuvõttu_määr*100, 2))+"%"
    
    # Katsetan tsüklis graafiku joonestamist
    axs[1].plot(np.array(x_list), pts)
    axs[1].set_xlabel('Iteratsioonid',fontsize=12)
    axs[1].set_title('Metropolis-Hastings \u03B8-le ', fontsize=24)
    axs[1].set_ylabel('\u03B8',fontsize=48, rotation=0)
    axs[1].set(xlim=(0, iteratsioonid), ylim=(0,1))
    axs[1].plot(samm,teeta, marker="o",markerfacecolor=marker_värv, markersize=10)
    axs[1].text(10,0.9, graafiku_text, style='italic',fontsize=24,
        bbox={'facecolor': marker_värv, 'alpha': 0.5, 'pad': 10})
    axs[1].text(10, 0.78, graafiku_text_2, fontsize=24)
    axs[1].text(10, 0.7, vvm_text, fontsize=24)
  
    
    
    bins_list = list(np.linspace(0,1,num=41))
    axs[0].hist(pts, bins=bins_list, orientation="horizontal") # orientation="horizontal" kui soovid graafikut ümber lükkata
    axs[0].set_title('Parameetri \u03B8 jaotus', fontsize=24)
    axs[0].get_xaxis().set_visible(False)
    axs[0].set_xlim([0,100])
    axs[0].set_ylim([0,1])
    axs[0].invert_xaxis() 
    axs[0].yaxis.set_ticks_position("right")
    axs[0].text(95,0.9, graafiku_text, style='italic',fontsize=24,
        bbox={'facecolor': marker_värv, 'alpha': 0.5, 'pad': 10})
    axs[0].text(95, 0.78, graafiku_text_2, fontsize=24)
    axs[0].text(95, 0.7, vvm_text, fontsize=24)
    axs[0].plot(0,teeta, marker="o",markerfacecolor=marker_värv, markersize=10,clip_on=False)
    plt.pause(0.1)
    
    if i != (iteratsioonid-1): # Selleks, et lõpus jääks graafik ekraanile
        axs[0].clear()
        axs[1].clear()
        
    samm+=1
  
plt.show()
vastuvõttu_määr=vastuvõtmiste_arv/iteratsioonid
print("Vastuvõttu määr on: " + str(vastuvõttu_määr*100)+"%")