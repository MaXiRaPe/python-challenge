# Module 3 Python Challenge
## PyBank exercise


import os
import csv
## Create a variable to call your data source
budgetdata_csv = r"C:\Users\ramir\python\python-challenge\PyBank\Resources\budget_data.csv"
## Create list variables to store data from columns of interest
dates = []
earnings = []
## create a list variable to store the calculated month to month change in profit/losses column
changes = []

## Open and read csv file
with open(budgetdata_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)
 ## Fill in the list variables from the csv file  
    for row in csvreader:
        dates.append(row[0])
        earnings.append(row[1])
 ## Use the length ('len') of the "dates" column as the total of months summarized in the data file     
    months = len(dates)
    print("\nFinancial Analysis\n \n-----------------------------\n ")
    print("Total Months: ", months)
       
 ## Calculate the month to month change in the profit/losses column   
    for i in range(len(earnings)-1):
        j=i+1
        change = int(earnings[j]) - int(earnings[i])
        changes.append(change)
  ## Calculate the average of the changes in the profit/losses       
    length = int(len(changes))
    total2 = int(sum(changes))
    avg = total2/length
  ## Modify the format of the values while printing the results  
    print("\nAverage Change: $", "%.2f" % float(avg))

  ## Find the maximum and minimum values in the changes list and match to the corresponding month.  The 'changes' list's lenght is shorter by one entry from the original data set. 
    max_increase = max(changes)
    m1 = int(changes.index(max_increase)) + 1
    month1 = dates[m1]
    max_decrease = min(changes)
    m2 = int(changes.index(max_decrease)) +1
    month2 = dates[m2]

    print("\nGreatest increase in Profits: ", month1, "  ($", int(max_increase), ")")
    print("\nGreatest decrease in Profits: ", month2, "  ($", int(max_decrease), ")\n")

## Create the .txt file using open and write/'w'
file_out = open(r'C:\Users\ramir\python\python-challenge\PyBank\analysis\PyBank.txt', 'w')
file_out.write("\nFinancial Analysis\n \n-----------------------------\n ")

file_out.write(f'\nTotal Months: {months}\n')
file_out.write(f'\nAverage Change: ${"%.2f" % float(avg)}\n')
file_out.write(f'\nGreatest increase in Profits: {month1}  (${int(max_increase)})\n')
file_out.write(f'\nGreatest decrease in Profits: {month2}  (${int(max_decrease)})\n') 
    
file_out.close()
