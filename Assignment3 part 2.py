import csv
import pprint
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#creating lists to keep track of the various titles
name = []
purpose = []
# reading my csv file from the previous part
with open('FE595_HW3_part1.csv') as compilation:
    compilation_data = csv.reader(compilation)
    for row in compilation_data:
        if row[1] != "Name":
            x = row[1]
            y = row[2]
            name.append(x)
            purpose.append(y)
# creating data frame
data = pd.DataFrame({"Name": name, "Purpose": purpose})
# sentiment analysis
analyzer = SentimentIntensityAnalyzer()
score = []
for i in range(200):
    x = analyzer.polarity_scores(purpose[i]).get('compound')
    score.append(x)
# adding compound score from sentiment analysis to 'data' dataframe
data['Compound_Score'] = score
# finding row with maximum compound score
print("The company with the highest compound score after conducting Sentiment Analysis is: \n")
pprint.pprint(data[data.Compound_Score == data.Compound_Score.max()])
print("\n")
# finding row with minimum compound score
print("The companies with the lowest compound score after conducting Sentiment Analysis is: \n")
pprint.pprint(data[data.Compound_Score == data.Compound_Score.min()])
print("\n")