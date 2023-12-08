

import csv
petiteagglo=["Appoigny","Auxerre", "Monéteau", "Perrigny", "Saint-Georges-sur-Baulche"]
grandeagglo=["Appoigny", "Augy", "Auxerre", "Bleigny-le-Carreau", "Branches", "Champs-sur-Yonne", "Charbuy","Chevannes", "Chitry", "Coulanges-la-Vineuse", "Escamps", "Escolives-Sainte-Camille", "Gurgy","Gy-l'Évêque", "Irancy", "Jussy", "Lindry", "Monéteau", "Montigny-la-Resle", "Perrigny","Quenne","Saint-Bris-le-Vineux", "Saint-Georges-sur-Baulche", "Vallan", "Venoy", "Villefargeau", "Villeneuve-Saint-Salves", "Vincelles", "Vincelottes"]
codepetit=[ "89380","89024","89470","89295","89346"]
codegrand=["89017", "89025", "89024", "89047", "89056", "89074", "89075", "89100", "89101", "89119",
    "89156", "89157", "89184", "89186", "89203", "89213", "89229", "89263", "89268", "89299",
    "89320", "89345", "89349", "89428", "89436", "89450", "89460", "89462", "89463"]
a=0
b=0
c=0
d=0
e=0
f=0
table2008=[]
table2016=[]
table2021=[]
with open ("donnees_2008.csv",newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=",")
    for row in reader:
        table2008.append(row)
for i in range(len(table2008)):
    if table2008[i][6] in petiteagglo and table2008[i][2] == "89" :
        #print([table2008[i][6]])
        a = a + int(table2008[i][7])

print ("La petite agglo compte " + str(a) +" habitant communaux en 2008")


for i in range(len(table2008)):
    if table2008[i][6] in grandeagglo and table2008[i][2] == "89" :
        #print([table2008[i][6]])
        b = b + int(table2008[i][7])
        
        
print("La grande agglo compte " + str(b) +" habitant communaux en 2008")








with open ("donnees_2016.csv",newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=",")
    for row in reader:
        table2016.append(row)
for i in range(len(table2016)):
    if table2016[i][6] in petiteagglo and table2016[i][2] == "89" :
        
        c = c + int(table2016[i][7])

print ("La petite agglo compte " + str(c) +" habitant communaux en 2016")


for i in range(len(table2016)):
    if table2016[i][6] in grandeagglo and table2016[i][2] == "89" :
        
        d = d + int(table2016[i][7])
        
        
print("La grande agglo compte " + str(d) +" habitant communaux en 2016")










with open ("donnees_2021.csv",newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=";")
    for row in reader:
        table2021.append(row)

for i in range(len(table2021)):
    if table2021[i][2] in codepetit :
        
        e = e + int(table2021[i][3])

print ("La petite agglo compte " + str(e) +" habitant communaux en 2021")


for i in range(len(table2021)):
    if table2021[i][2] in codegrand :
        
        f = f + int(table2021[i][3])
        
        
print("La grande agglo compte " + str(f) +" habitant communaux en 2021")