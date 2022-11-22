from ntpath import join
from pyexpat import model
import random as rd
from pylab import *

def bilmerke():
    merkerModell={
    "Audi":["Etron","Q8","A1","A6","R8"],
    "Ford":["F150","Mondeo","Focus","E-Mach","Mustang"],
    "BMW":["IX","I3","I7","5-siries","X5"],
    "Mercedes":["EQC","EQS","AMG","C-Class","GLC"],
    "Hyundai":["Ionic","Ionic-5","Kona","Nexo","Tucson"]
    }
    o=rd.randint(0,4)
    u=rd.randint(0,4)
    lol1=[]
    lol2=[]
    for keys,values in merkerModell.items():
        lol=keys
        lol3=values
        lol1.append(lol)
        lol2.append(lol3)
    merke=lol1[o]
    modell=lol2[o][u]
    return merke,modell
print(bilmerke())


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += str(ele)
    return str1
def nummer():
    bokstav=["DN","EE","ED","DL","EK","CF"]
    minilist=[]
    sike=rd.randint(0,5)
    send=bokstav[sike]
    for i in range (5):
        midlist=rd.randint(0,9)
        minilist.append(midlist)
    complist=listToString(minilist)
    skilt=(send+complist)
    return skilt

navn=loadtxt("navnliste.csv", delimiter=";",dtype=str,encoding='utf-8-sig')
navnliste=navn
print(navnliste[0])
def eier(x):
     print(navnliste[x])
for i in range(len(navnliste)):
   eier(i)
with open("readme(1).txt","w") as f:
    for i in range(100):
        try:
            f.write((navnliste[i])+"\t"+nummer()+"\t"+bilmerke()[0]+"\t"+bilmerke()[1]+"\n")
        except:
            p=rd.randint(0,73)
            f.write((navnliste[p])+"\t"+nummer()+"\t"+bilmerke()[0]+"\t"+bilmerke()[1]+"\n")