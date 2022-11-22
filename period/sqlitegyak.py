import sqlite3
'''1.1 Feladat
Írj egy programot, amely SQLite adatbázisban tárolja ezen fájlban található adatokat!
Az adatokat nem kell feltélenül fájlból beolvasnia a programnak. A program olvassa ki az adatbázisból és listázza ki az adatokat!'''

#AtomicNumber,Element,Symbol,AtomicMass,NumberofNeutrons,NumberofProtons,NumberofElectrons,Period,Group,Phase,Radioactive,Natural,Metal,Nonmetal,Metalloid,Type,AtomicRadius,Electronegativity,FirstIonization,Density,MeltingPoint,BoilingPoint,NumberOfIsotopes,Discoverer,Year,SpecificHeat,NumberofShells,NumberofValence

con = sqlite3.connect("adatbazis.db")
cur = con.cursor()

class Valami:
    def __init__(self, sor):
        atomicnumber,element,symbol,atomicmass, *szemet = sor.strip().split(",")
        self.atomicnumber = atomicnumber
        self.element = element
        self.symbol = symbol
        self.atomicmass = atomicmass

with open("adat.csv") as f:
    fejlec = f.readline()
    adat = [Valami(sor) for sor in f]

cur.execute("DROP TABLE IF EXISTS period")
cur.execute("CREATE TABLE period(atomicnumber, element, symbol, atomicmass)")
for i in adat:
    lista = [(i.atomicmass, i.atomicnumber, i.element, i.symbol)]
    cur.executemany("INSERT INTO period VALUES(?,?,?,?)", lista)




#con.commit()
#barmi = cur.execute("SELECT * FROM period")
#print(barmi.fetchall())
#ugyan az mint az alsó csak az szebb

for sor in cur.execute("SELECT * FROM period"):
    print(sor)