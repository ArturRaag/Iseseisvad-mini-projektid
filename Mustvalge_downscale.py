from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


img=Image.open(r"_________________PATH TO IMAGE HERE__________________")

print(img.size)
laius, kõrgus = img.size
print(laius, kõrgus)

######################################[ ALTERNATIIV ]##################################################
def poolita_mustvalgeks(pilt, W, H): # <----------- Funktsiooni argumendid: (pilt, laius, kõrgus)
    kogu_kraam_mustvalge = []
    for i in range(1, H, 2):
        for j in range(1, W, 2):
            pildipunkt = pilt.getpixel((j,i))
            if len(pildipunkt)>1:
                pildipunkt = int((pildipunkt[0]+pildipunkt[1]+pildipunkt[2])/3)
            kogu_kraam_mustvalge.append(pildipunkt)
            
    pildi_maatriks = np.reshape(kogu_kraam_mustvalge, (int(H/2), int(W/2)))
    return pildi_maatriks
######################################[ ALTERNATIIV ]##################################################


plt.imshow(poolita_mustvalgeks(img, laius, kõrgus))
plt.show()

##uus_pilt=Image.fromarray(poolita_mustvalgeks(img, laius, kõrgus))
##uus_pilt.show()
