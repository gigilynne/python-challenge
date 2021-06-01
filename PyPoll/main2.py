#PyPoll

# import packages
import csv
import os

#define function to fix percentage format to 3 decimal points
def fixPercent(num):
    num = "{:.3%}".format(num)
    return num

#create paths for both the input and output files
inputfile = os.path.join("Resources", "election_data.csv")
outputfile = os.path.join("Analysis", "analysis.txt")

#create empty lists and variables for storing values and calculations from data
unique_can = []
tot_votes = []
per_votes = []
tot_votes = 0
win_count = 0

# read the CSV file
with open(inputfile, 'r') as electiondata:
    reader = csv.reader(electiondata, delimiter=",")

    #store header rows into a variable
    Headers = next(reader)

    #create a for loop to go through each row in the CSV file and count the total number of votes

    for row in reader:
        tot_votes += 1
    
        # get unique candidate names and individual vote counts and store in lists
        # if row[2] (candidate name) is not in the unique_can list, i.e. if it is the first instance of the name
        if row[2] not in unique_can:

            #append the name to unique_can and a value of 1 to tot_votes list
            unique_can.append(row[2])
            tot_votes.append(1)

        # if not,
        else:

            #get the index of the candidate from the unique_can list and the vote count by 1
            CandidateIndex = unique_can.index(row[2])
            tot_votes[CandidateIndex] += 1
        

# calculate percentage of votes for each candidate
for i in range(len(tot_votes)):
    per_votes.append(tot_votes[i] / tot_votes)

# calculate the winner based on most votes
for i in range(len(tot_votes)):

    # if the number of votes is greater than win_count (initially zero)
    if tot_votes[i] > win_count:
        
        #update win_count to the number of votes at index i
        win_count = tot_votes[i]

        #update winner to the candidate name at index i
        winner = unique_can[i]

# create a text file with the analysis output
with open(outputfile, 'w') as textfile:
    textfile.write(f"Election Results\n"
                   f"----------------------------\n"
                   f"Total Votes: {tot_votes}\n"
                   f"----------------------------\n"
                   )

    # for loop to iteratively write each candidate's info
    for i in range(len(unique_can)):
        textfile.write(f"{unique_can[i]}: {fixPercent(per_votes[i])} ({tot_votes[i]})\n")

    textfile.write(f"----------------------------\n"
                   f"Winner: {winner}\n"
                   f"----------------------------\n"
                  )

# create a text file and then read the output
with open (outputfile, 'r') as analysis:
    contents = analysis.read()
    print(contents)