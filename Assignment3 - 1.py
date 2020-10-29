# the libraries needed to solve this right now
import csv
import pandas as pd

#creating lists to keep track of the various titles
name = []
purpose = []


# opening and reading Aniruddh's csv file
with open('Assignment_2.csv') as ani:
    ani_data = csv.reader(ani)
    for row in ani_data:
        if row[1] != "Name":
            x = row[1]
            y = row[2]
            name.append(x)
            purpose.append(y)

# reading Simran's csv file
with open('Simran_results_Assignment2.csv') as simran:
    simran_data = csv.reader(simran)
    for row in simran_data:
        if row[1] != "Name":
            x = row[1]
            y = row[2]
            name.append(x)
            purpose.append(y)


# reading my txt file
with open('Results2.txt') as vaikunth:
    a = vaikunth.read()
    b = a.split("\n")
    for i in b:
        if 'Name: ' in i:
            x = i[6:]
            name.append(x)
        if 'Purpose: ' in i:
            y = i[9:]
            purpose.append(y)


# reading Kshitij's txt file
with open('WebScrOutput.txt') as kshitij:
    a = kshitij.read()
    b = a.split("\n")
    for i in b:
        if 'Name: ' in i:
            x = i[6:]
            name.append(x)
        if 'Purpose: ' in i:
            y = i[9:]
            purpose.append(y)

#creating a dataframe with all the names and purposes
finalproduct = pd.DataFrame({"Name": name, "Purpose": purpose}, index=range(1, 201))
finalproduct.to_csv('FE595_HW3_part1.csv')
