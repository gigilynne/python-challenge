#main.py
## PyBank

#import modules
import os
import csv

#set a path for the csv file using the join for both windows and mac os
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

#set all variables to zero before opening the files so they are ready to go as the code begins
months = 0
profits = 0


#open and then read the csv - attemped to only open as csv, but will move to open directly into reading as a dictionary file
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #read the header row because they exist
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

#need to interpret the details in the csv for analysis and return the totals for months, total profits, change in profits by accreting each through a for loop

    for row in csv_reader:
        months += 1
        profits += int(row[1])
        
    #Print the details in the format needed
    print(months)
    print(profits)
    print(profits/months)

#Return the highest number in (row[1]) and zip to (row[0]) 


#Return the lowest number in (row[1]) and zip to (row[0]) 

# # Specify the file to write to
# output_path = os.path.join(Analysis", "analysis.txt")

# # Open the file using "write" mode. Specify the variable to hold the contents and open the file to write
# with open(output_path,"analysis.txt", 'w',):
#     f = open(analysis.txt)

#     #Set the Header row for the table analysis
#     f.write("Financial Analysis")
#     f.write("------------------------------")

#     # Write the first data row - pass the sum of the total of the total months into the written file
#     f.write("Total Months:", months)

#     # Write the second row - pass the net total amount of the "Profit/Losses" over the entire period into the written file
#     f.write("Total: $", profits)

#     # Write the third row - pass the changes in Profits over the entire period into the written file
#     f.write("Average Change: $", profits/months)

#     # Write the fourth row - pass the net total amount of the Greatest Increase in Profits over the entire period into the written file
#     f.write("Greatest Increase in Profits:", "x", "x")

#     # Write the fifth row - pass the net total amount of the Greatest Decrease in Profits over the entire period into the written file
#     f.write("Greatest Decrease in Profits:", "x", "x")
#     f.close()

