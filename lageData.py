from ntpath import join
from pyexpat import model
import random as rd
from pylab import *

def bilmerke(): #Funksjonen lager en tilfeldig sammensetning av merke og modell som hører sammen
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
        lol=keys #keys vil si hovednavnene altså merkene
        lol3=values #values er verdiene for merkene altså modellene
        lol1.append(lol)
        lol2.append(lol3)
        print(lol)
    merke=lol1[o]
    modell=lol2[o][u]
    final=[]
    return merke,modell #returnerer en tuple som kan brukes som en liste
print(bilmerke()) #vil printe ([merke,modell])


def listToString(s):#en funksjon som gjør om en liste med verdier til en string
    str1 = ""
    for ele in s:
        str1 += str(ele)
    return str1
def nummer(): #genererer et regestreringsnummer for bilen med en satt sammensetning med bokstaver og en tilfeldig liste med 5 tall.
    bokstav=["DN","EE","ED","DL","EK","CF"]
    minilist=[]
    sike=rd.randint(0,5)
    send=bokstav[sike]
    for i in range (5):
        midlist=rd.randint(0,9)
        minilist.append(midlist)
    complist=listToString(minilist)
    skilt=(send+complist)
    return skilt#returnerer en string hvor nummeret består av 2bokstaver og 5tall

navn=loadtxt("navnliste.csv", delimiter=";",dtype=str,encoding='utf-8-sig')#laster en liste med 74 tall
navnliste=navn#gjør om dokumentet til en liste med navn
def eier(x): #funksjonen setter sammen en sammenkobling av eier, reg nummer og merke, modell.
     print(navnliste[x])
for i in range(len(navnliste)):
   eier(i)
with open("readme(1).txt","w") as f:#opretter/redigerer ett dokument hvor den kjører løkken 100 ganger og skriver inn genererte verdier.
    for i in range(100):
        impCar=bilmerke()#for at modell og merke skal samkjøres kan funksjonen bare bli kjørt en gang og generere en satt liste for hver gang den skal printe en verdi.
        try:
            f.write((navnliste[i])+"\t"+nummer()+"\t"+impCar[0]+"\t"+impCar[1]+"\n")
        except:#navnlisten er på 74 navn og det vil være nødvendig med 100 biler med 100 eiere. derfor kjøres løkken til dette er oppfylt med genbruk av navn
            p=rd.randint(0,73)
            f.write((navnliste[p])+"\t"+nummer()+"\t"+impCar[0]+"\t"+impCar[1]+"\n")