import sqlite3
2
'''1.1 Feladat
3
Írj egy programot, amely SQLite adatbázisban tárolja ezen fájlban található adatokat!
4
Az adatokat nem kell feltélenül fájlból beolvasnia a programnak. A program olvassa ki az adatbázisból és listázza ki az adatokat!'''
5
​
6
#AtomicNumber,Element,Symbol,AtomicMass,NumberofNeutrons,NumberofProtons,NumberofElectrons,Period,Group,Phase,Radioactive,Natural,Metal,Nonmetal,Metalloid,Type,AtomicRadius,Electronegativity,FirstIonization,Density,MeltingPoint,BoilingPoint,NumberOfIsotopes,Discoverer,Year,SpecificHeat,NumberofShells,NumberofValence
7
​
8
con = sqlite3.connect("adatbazis.db")
9
cur = con.cursor()
10
​
11
class Valami:
12
    def __init__(self, sor):
13
        atomicnumber,element,symbol,atomicmass, *szemet = sor.strip().split(",")
14
        self.atomicnumber = atomicnumber
15
        self.element = element
16
        self.symbol = symbol
17
        self.atomicmass = atomicmass
18
​
19
with open("adat.csv") as f:
20
    fejlec = f.readline()
21
    adat = [Valami(sor) for sor in f]
22
​
23
cur.execute("DROP TABLE IF EXISTS period")
24
cur.execute("CREATE TABLE period(atomicnumber, element, symbol, atomicmass)")
25
for i in adat:
26
    lista = [(i.atomicmass, i.atomicnumber, i.element, i.symbol)]
27
    cur.executemany("INSERT INTO period VALUES(?,?,?,?)", lista)
28
​
29
​
30
​
31
​
32
#con.commit()
33
#barmi = cur.execute("SELECT * FROM period")
34
#print(barmi.fetchall())
35
#ugyan az mint az alsó csak az szebb
36
​
37
for sor in cur.execute("SELECT * FROM period"):
38
    print(sor)
