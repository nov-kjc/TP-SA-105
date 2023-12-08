import csv
table=[]
population_2008 = 0
population = ""
grande_agglo = ["Appoigny","Augy", "Auxerre", "Bleigny-le-Carreau", "Branches", "Champs-sur-Yonne", "Charbuy","Chevannes", "Chitry", "Coulanges-la-Vineuse", "Escamps", "Escolives Sainte-Camille", "Gurgy","Gy-l'Évêque", "Irancy", "Jussy", "Lindry", "Monéteau", "Montigny-la-Resle", "Perrigny", "Quenne","Saint-Bris-le-Vineux", "Saint-Georges-sur-Baulche", "Vallan", "Venoy", "Villefargeau", "Villeneuve-Saint-Salves", "Vincelles", "Vincelottes"]
numéro_de_commune =  ["89017", "89025", "89024", "89047", "89056", "89074", "89075", "89100", "89101", "89119","89156", "89157", "89184", "89186", "89203", "89213", "89229", "89263", "89268", "89299","89320", "89345", "89349", "89428", "89436", "89450", "89460", "89462", "89463"]


with open ("donnees_2008.csv",newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=",")
    for row in reader:
        table.append(row)


for i in range(len(table)): 
    if table[i][6] in grande_agglo and table[i][2] == "89":
        
        population = table[i][9]
        population = int(population)
        population_2008 += population

print("population 2021 grande agglomération= ",population_2008)

table2=[]
population_2016 = 0
population2 = ""

with open ("donnees_2016.csv",newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=",")
    for row in reader:
        table2.append(row)


for i in range(len(table2)): 
    if table2[i][6] in grande_agglo and table2[i][2] == "89":
        
        population2 = table2[i][9]
        population2 = int(population2)
        population_2016 += population2

print("population 2016 grande agglomération= ",population_2016)

table3=[]
population_2021 = 0
population3 = ""

with open ("donnees_2021.csv",newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=";")
    for row in reader:
        table3.append(row)


for i in range(len(table3)):
    if table3[i][2] in numéro_de_commune:
        
        population3 = table3[i][5]
        population3 = int(population3)
        population_2021 += population3

print("population 2021 grande agglomération= ",population_2021)