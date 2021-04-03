#main.py

## PyBank

#import modules
import os
import csv

#set a path for the csv file using the join for both windows and mac os
budget_data_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#open and then read the csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #read the header row because they exist
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

