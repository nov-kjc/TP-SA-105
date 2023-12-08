import csv
table=[]
population_2008 = 0
population = ""
with open ("donnees_2008.csv",newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=",")
    for row in reader:
        table.append(row)


for i in range(len(table)):

    if table[i][6] == "Auxerre"or table[i][6] == "Appoigny" or table[i][6] == "Monéteau" or table[i][6] == "Perrigny" or table[i][6] == "Saint-Georges-sur-Baulche" and table[i][2] == "89":
        
        population = table[i][9]
        population = int(population)
        population_2008 += population

print("population 2008 petite agglomération= ",population_2008)




table2=[]
population_2016 = 0
population2 = ""
with open ("donnees_2016.csv",newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=",")
    for row in reader:
        table2.append(row)

for i in range(len(table2)):
    if table2[i][6] == "Auxerre" or table2[i][6] == "Appoigny" or table2[i][6] == "Monéteau" or table2[i][6] == "Perrigny" or table2[i][6] == "Saint-Georges-sur-Baulche" and table2[i][2] == "89" :
        population2 = table2[i][9]
        population2 = int(population2)
        population_2016 += population2

print("population 2016 petite agglomération= ",population_2016)

table3=[]
population_2021 = 0
population3 = ""
with open ("donnees_2021.csv",newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=";")
    for row in reader:
        table3.append(row)


for i in range(len(table3)):
    if table3[i][2] == "89024" or table3[i][2] == "89013" or table3[i][2] == "89263" or table3[i][2] == "89295" or table3[i][2] == "89346":
        population3 = table3[i][5]
        population3 = int(population3)
        population_2021 += population3

print("population 2021 petite agglomération= ",population_2021)

