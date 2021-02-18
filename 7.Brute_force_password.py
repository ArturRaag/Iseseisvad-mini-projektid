# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 03:38:54 2021

@author: artur
"""

import numpy as np
tähestik=list("abcdefghijklmnopqrsšžztuvwõäöüxy")
password="xx"
pakkumine=""
loendaja=0
while password!=pakkumine:
    pakkumine=""
    pikkus=len(password)
    random_parool=np.random.choice(tähestik,pikkus)
    pakkumine_uus=[]
    for i in random_parool:
        pakkumine_uus.append(i)
    pakkumine="".join(pakkumine_uus)
    loendaja=loendaja+1
print("Parool saadi {}-ndal katsel ning see on: {}".format(loendaja,pakkumine))
