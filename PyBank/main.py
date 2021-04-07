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
net_change_list = []

#open and then read the csv - attemped to only open as csv, but will move to open directly into reading as a dictionary file
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #read the header row because they exist
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    #skip the first row since there is no change that month
    first_row = next(csv_reader)

    previous = first_row[1]


#need to interpret the details in the csv for analysis and return the totals for months, total profits, and change in profits by accreting each through a for loop
    for row in csv_reader:
        months += 1
        profits += int(row[1])

        net_change = int(row[1]) - previous

        previous = int(row[1])

        net_change_list += [net_change]

        
    #Print the details in the format needed
    print(months)
    print(profits) 
    print(round(profits/months, 2))

#Return the highest number in (row[1]) and zip to (row[0]) 
    #for x in range (row[1])
    increase = max(net_change_list)
    print(increase)

#Return the lowest number in (row[1]) and zip to (row[0]) 
    decrease = min(net_change_list)
    print(decrease)

# Specify the file to write to
output_path = os.path.join('Analysis', "analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents and open the file to write
with open(output_path, 'w'):
    f = open(analysis.txt)

    #Set the Header row for the table analysis
    f.analysis.write("Financial Analysis")
    f.analysis.write("------------------------------")

    # Write the first data row - pass the sum of the total of the total months into the written file
    f.analysis.write("Total Months:", months)

    # # Write the second row - pass the net total amount of the "Profit/Losses" over the entire period into the written file
    # f.write("Total: $", profits)

    # # Write the third row - pass the changes in Profits over the entire period into the written file
    # f.write("Average Change: $", profits/months)

    # # Write the fourth row - pass the net total amount of the Greatest Increase in Profits over the entire period into the written file
    # f.write("Greatest Increase in Profits:", increase)

    # # Write the fifth row - pass the net total amount of the Greatest Decrease in Profits over the entire period into the written file
    # f.write("Greatest Decrease in Profits:", decrease)
    # f.close()

