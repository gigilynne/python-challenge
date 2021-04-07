#main1.py

## PyPoll

#import modules
import os
import csv

#set a path for the csv file using the join for both windows and mac os
budget_data_csv = os.path.join('Resources', 'election_data.csv')

#open and then read the csv - attemped to only open as csv, but will move to open directly into reading as a dictionary file
with open(budget_data_csv) as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=",")

   #read the header row because they exist
   csv_header = next(csv_file)
   print(f"Header: {csv_header}")
 
  #create a dictionary for the csv, with the voter ID as the key 
  
  #calucluate the total number of votes cast

  #use the dictionary to create a list of candidates who received votes

  #use the created list and the calculated total of votes to determine the percentage of votes each candidate won

  #use the dictionary to return the total number of votes each candidate won

  #use the value from the list created above to determine the winner of the election based on popular vote

  #use f-strings to print the values in the required format

# Specify the file to write to
output_path = os.path.join('Analysis', "analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents and open the file to write
with open(output_path, 'w'):
    f = open(analysis.txt)

#write out the analysis in the required format for review in the .txt file