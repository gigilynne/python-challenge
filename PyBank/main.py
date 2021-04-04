#main.py

## PyBank

#import modules
import os
import csv

#set a path for the csv file using the join for both windows and mac os
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

#open and then read the csv - attemped to only open as csv, but will move to open directly into reading as a dictionary file
#with open(budget_data_csv) as csv_file:
 #   csv_reader = csv.reader(csv_file, delimiter=",")

    #read the header row because they exist
 #   csv_header = next(csv_file)
 #   print(f"Header: {csv_header}")

#create a dictionary from the csv
with open('budget_data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            total = 0.0
            for number in numbers:
                total += number
            print(f'Total {": ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')

# Write a function that returns the arithmetic sum for a list of numbers
numbers = [(Profit/Losses)]
    sum = sum(numbers)
    print(f'Total Months:' sum)






# Specify the file to write to
output_path = os.path.join("..", "Analysis", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    #Set the Header row for the table analysis
    csvwriter.writerow(['Financial Analysis'])
    
    # Write the first data row - pass the sum of the total of the total months into the written file
    csvwriter.writerow(['Total Months': "x"])

    # Write the second row - pass the net total amount of the "Profit/Losses" over the entire period into the written file
    csvwriter.writerow(['Total':"X"])

    # Write the third row - pass the net total amount of the Greatest Increase in Profits over the entire period into the written file
    csvwriter.writerow(['Total':"X"])

    # Write the fourth row - pass the net total amount of the Greatest Decrease in Profits over the entire period into the written file
    csvwriter.writerow(['Total':"X"])
