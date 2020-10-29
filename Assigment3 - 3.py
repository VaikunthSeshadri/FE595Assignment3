import csv
import pandas as pd
from collections import Counter


#creating lists to keep track of the various titles

name = []
purpose = []
# reading my csv file from part 1
with open('FE595_HW3_part1.csv') as compilation:
    compilation_data = csv.reader(compilation)
    for row in compilation_data:
        if row[1] != "Name":
            x = row[1]
            y = row[2]
            name.append(x)
            purpose.append(y)
# creating data frame
data = pd.DataFrame({"Name": name, "Purpose": purpose}, index=range(1, 201))
# creating list of tokens
token = {}
def frequency_of_token(text):
    words = text
    words = words.split()
    for t in words:
        if t not in token:
            token[t] = 0
        token[t] += 1
    return token
for i in purpose:
    frequency_of_token(i)
frequency = Counter(token)
top_ten = frequency.most_common(10)
print("10 most common words:")
for i in top_ten:
    print(i[0], "-", i[1], " ")