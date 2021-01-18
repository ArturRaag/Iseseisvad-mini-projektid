# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:39:21 2020

@author: artur
"""

# THEME OF THE GAME: INSTEAD OF SEARCHING FOR LIGHT/JOY (SUN) EXTERNALLY, TRY AND SEARCH IT FROM WITHIN (DEEP DARK DUNGEON FILLED WITH DIFFICULT CHALLENGES, MYSTERIES AND RIDDLES).

import sys
from time import sleep
from os import startfile

paus="\n___________________________________________________________________________________________________________________________________________"

print("\n\nJÄLITAJA"+"\n__________________\n\n")

a1="On varahommik, ning maapind on kaetud tiheda lumega. Õhk on külm ning väga kuiv, mis teeb hingamise valusaks. Sa oled mitmeid nädalaid kõndinud külmetava päikese järel, ja vaikselt tekkib kahtlus, et ehk oled käinud ringimööda. Kuid kahtlus vaibub kähku, kuna meenub, et ise enda mahajäetud jälgi maapinnal märganud ei ole.\n\n\nHorisondil märkad veidrat lehvivat kuju. Kuna oled oma teekonna käigus juba sääraseid miraaže kohanud, siis ei kiirusta sa kohe rõõmustama. Eeldad, et on tegemist järjekordse puuga, mille külge jäi ripuma kellegi mahajäetud pesu. Sellest hoolimata, jääd ikkagi mõttesse ja kaalud, kas läheneda kujule või jätkata enda teekonda päikese järel.\n"

# for char in a1:
#     sleep(0.075)
#     sys.stdout.write(char)

print(a1+paus)


while True:
    try:
        input_1 = (str(input("Kas jätkad päikese jälitamist [1] või lähened veidrale kujule [2]?\n" ))).strip()
        if input_1 == ("2"):
            option_1 = "Otsustasid liikuda kuju suunas. \nAstud aeglaselt kuju poole, kuid iga sammuga suureneb sinus kõhklus. Maapinnalt märkad, et iga sammuga muutub sinu vari pikkemaks ja suuremaks. See tähelepanek hirmutab sind. Sa ei ole kindel miks, kuid ehk on see sellepärast, et kardad lihtsalt valgusest ilma jääda. Samas igatsed sa väga teisi inimesi.\n\nJääd hetkeks seisma ja kartusest valgusest ilma jääda, mõtled minna tagasi Päikest jälitama.\n"
            break
            # while True:
            #     try:
            #         input_2=(str(input("Mida otsustad?\n\n[1] Lähen tagasi Päikest jälitama.\n[2] Ei. Ma olen lõplikult otsustanud. Tahan teada mis või kes see kuju on.\n\n"))).strip()
            #         if input_2==("2"):
            #             edasi1=("Otsustad Päikest hüljata, ja sammud nüüd kiiruga kuju suunas.")
            #             for char in edasi1:
            #                 sleep(0.075)
            #                 sys.stdout.write(char)
            #             break
            #         elif input_2==("1"):
            #             tagasi1="Otsustasid minna tagasi Päikest jälitama."
            #             for char in tagasi1:
            #                 sleep(0.075)
            #                 sys.stdout.write(char)
            #             input_1=("1")
                        
            #         else:
            #             1/0
                        
            #     except:
            #         viga2="Selline variant ei sobi. Vali kas variant [1] või [2]."
            #         for char in viga2:
            #             sleep(0.075)
            #             sys.stdout.write(char) 
        elif input_1==("1"):
            option_1="Otsustasid haruldast kuju ignoreerida ja jätkata Päikese jälitamist.\n\n Järgnevad päevad kulusid sul Päikese jälitamisele. Ühel õnnetul päeval neelasid aga tumedad pilved Päikese alla ja sul ei õnnestunud enam millegi järgi orienteeruda. Hämmingus, otsustasid ikkagi edasi sammuda. Järgnes aga lumetorm, mis viis sind eksiteele ja lõpuks avastad, et jõudsid tagasi kohta, kus eelnevalt olid. Eemal märkad taas ka seda sama lehvivat kuju, kuid sel korral on tema asukoht teiste lähestiku olevate objektide suhtes nihkunud.\n Lumetorm on vaibunud, ning Päikese sära on taas pilvede vahelt näha. Hakkad viivitamatult uuesti sammuma Päikese suunas, kuid pead korraks seisma ja vaatad uuesti veidra kuju suunas.\n"
            # print(option_1)
            print(paus)
            for char in option_1:
                sleep(0.075)
                sys.stdout.write(char)
            print(paus)
        else:
            1/0
    except:
        viga1="Selline variant ei sobi. Vali kas variant [1] või [2]."
        print(paus)
        for char in viga1:
            sleep(0.075)
            sys.stdout.write(char)
        print(paus)
        
    
if input_1 == ("2"):
    startfile(r"C:\Users\artur\Desktop\Atmosphere\Der Weinende Hadnur.mp3")   # See käsk avab faili Pathist. Faili pathi kopeerimiseks kasuta: Shift-> Right Click -> Copy as Path
    print(paus)
    for char in option_1:
        sleep(0.075)
        sys.stdout.write(char)
    print(paus)
        
    while True:
        try:
            input_2=(str(input("Mida otsustad?\n\n[1] Lähen tagasi Päikest jälitama.\n[2] Ei. Ma olen lõplikult otsustanud. Tahan teada mis või kes see kuju on.\n\n"))).strip()
            if input_2==("2"):
                edasi1=("""Otsustad Päikest hüljata, ja sammud nüüd kiiruga kuju suunas.\n
Lähemale jõudes mõistad, et tegemist on tõepoolest inimesega.
Sa rõõmustad, ning asud ekstaasis käsi lehvitama, häälitsema ning üle lumehangede kopperdades kiirema sammuga tegelase poole liikuma.
Paned ka tähele, et tegelase kõrval asub märkimisväärne maalõhe. Eeldad, et tegemist on tema elupaigaga.
Lõpuks jõuad temani, kuid sa pole päris kindel, kas tegelane ärkvelgi on.



Lõpuks möödas on suvi,
justkui olnudki poleks.
Päike kiirgab veel soojust,
kuid vaid sellest on vähe.

Kõik mis tõeks võis saada,
nagu leheke liugles,
mul käe vahele langes.
Kuid ka sellest on vähe.

Ei õelus ei kurjus,
ega headus maalt kadus.
Kõik säras vaid valgelt.
Kuid ka sellest on vähe.

Mul lehed veel õitsevad
Ning oksad on terved.
Päev on selge kui klaas.
Kuid ka sellest on vähe.

Elu mind tiiva alla võttis.
Hoolitses ja päästis.
Mul on tõesti vedanud.
Ent ka sellest on vähe.

""")
                print(paus)
                for char in edasi1:
                    sleep(0.075)
                    sys.stdout.write(char)
                print(paus)
                
                
                
                
                break
            elif input_2==("1"):
                tagasi1="Otsustasid minna tagasi Päikest jälitama.\nSee otsus osutus sulle saatuslikuks kuna sattusid järjekordselt lumetormi ja surid külma kätte.\n"
                print(paus)
                for char in tagasi1:
                    sleep(0.075)
                    sys.stdout.write(char)
                print(paus)
                break
            else:
                1/0
        except:
            viga2="Selline variant ei sobi. Vali kas variant [1] või [2].\n"
            print(paus)
            for char in viga2:
                sleep(0.075)
                sys.stdout.write(char)
            print(paus)
else:
    pass

#if input_2==("2"):
    