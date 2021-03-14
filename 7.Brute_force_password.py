
import time
import numpy as np

start=time.time()
tähestik=list("abcdefghijklmnopqrsšžztuvwõäöüxy")
password="pass"
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
    print("Katse iteratsioon: "+ str(loendaja)+". Pakutud parool: " +str(pakkumine))
end=time.time()
print("Parool saadi {}-ndal katsel ning see on: {}.\nAega kulus: {} sekundit.".format(loendaja,pakkumine,(round((end-start),2))))

