# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 03:39:24 2020

@author: artur
"""

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

bw=np.eye(10,10)
bw[3,2]=0.5
bw[5,1]=0.25
bw[1,9]=0.1

plt.imshow(bw, cmap=cm.Greys_r)

red=np.zeros((10,10), dtype=np.int64) # Punane "kiht"
green=np.zeros((10,10), dtype=np.int64) # Roheline "kiht"
blue=np.zeros((10,10), dtype=np.int64) # Sinine "kiht"

red[2,2]=255
green[5,5]=255
blue[9,9]=255

red[3,7]=120
green[3,7]=55

# colimg=np.array([red,green,blue]) #Transponeerimata: "TypeError: Invalid shape (3, 10, 10) for image data"

colimg=np.array([red,green,blue]).T
print(colimg.shape)
print(colimg)
plt.imshow(colimg)
