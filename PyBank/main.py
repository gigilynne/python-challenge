
#  import packages to read/write CSV files, create a dynamic path to the file and mean calculation 
import csv
import os
import statistics as st #to calculate average

# define function to calculate average of the list 
def Average(list):

    #  round the number to 2 decimal points and return value 
    return round(st.mean(list), 2) 

#open and then read the csv - attemped to only open as csv, but will move to open directly into reading as a dictionary file
inputfile = os.path.join("Resources", "budget_data.csv")
outputfile = os.path.join("Analysis", "analysis.txt")

#  create empty lists for storing values and calculations from data 
Dates = []
profit_loss = []
pl_change = []

#  read the CSV file and store values of each column into lists 
with open(inputfile, 'r') as budgetdata:
    reader = csv.reader(budgetdata, delimiter=",")
    
    #  store header rows into a Headers list 
    Headers = next(reader)

    #  for loop to go through each row in the CSV file and append values from date column to the 'Dates' list and Profits/Losses column to the 'profit_loss' list 
    for row in reader:
        Dates.append(row[0])
        profit_loss.append(int(row[1]))

#  for loop to go through each value in Profits/Losses list and calculate total 
totalprofit_loss = 0
for i in profit_loss:
    totalprofit_loss = i + totalprofit_loss

#  use list comprehension to create a new list with difference values of each successive row (next row - current row) 
pl_change = [profit_loss[i+1] - profit_loss[i] for i in range(0,len(profit_loss)-1)]

#  calculate average change by calling the function and store in variable 
AverageChange = Average(pl_change)

#  insert a value of zero at index 0 of the pl_change list as there is no previous data to subtract for the first month (thus also making the list equal in length to Dates and profit_loss lists for index finding later) 
pl_change.insert(0,0)

#  initialize greatest increase/decrease variables to 0 
g_increase = 0
g_decrease = 0

#  for loop to calculate greatest increase and decrease in profits and losses 
for i in range(len(pl_change)-1):
    if pl_change[i] < g_decrease:
        g_decrease = pl_change[i]

    if pl_change[i] > g_increase:
        g_increase = pl_change[i]   


#  find the index for the greatest increase and decrease in profits and losses 
GIindex = pl_change.index(g_increase)
GDindex = pl_change.index(g_decrease)

#  find the corresponding date of the greatest increase and decrease amounts using GI/GD indexes found above 
GIdate = Dates[GIindex]
GDdate = Dates[GDindex]
    
# create a text file and then read the output
with open(outputfile, 'w') as textfile:
    textfile.write(f"Financial Analysis\n"
                   f"---------------------------\n"
                  f"Total Months: {len(Dates)}\n"
                  f"Total: ${totalprofit_loss}\n"
                  f"Average Change: ${AverageChange}\n"
                  f"Greatest Increase in Profits: {GIdate} (${g_increase})\n"
                  f"Greatest Decrease in Profits: {GDdate} (${g_decrease})\n"
)

with open (outputfile, 'r') as analysis:
    contents = analysis.read()
    print(contents)
