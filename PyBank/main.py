# Module 3 Python Challenge
## PyBank exercise


import os
import csv

budgetdata_csv = r"C:\Users\ramir\python\python-challenge\PyBank\Resources\budget_data.csv"
dates = []
earnings = []
changes = []

# Open and read csv
with open(budgetdata_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)
    
    for row in csvreader:
        dates.append(row[0])
        earnings.append(row[1])
        
    months = len(dates)
    print("\nFinancial Analysis\n \n-----------------------------\n ")
    print("Total Months: ", months)
       
    
    for i in range(len(earnings)-1):
        j=i+1
        change = int(earnings[j]) - int(earnings[i])
        changes.append(change)
         
    length = int(len(changes))
    total2 = int(sum(changes))
    avg = total2/length

    print("\nAverage Change: $", "%.2f" % float(avg))

    
    max_increase = max(changes)
    m1 = int(changes.index(max_increase)) + 1
    month1 = dates[m1]
    max_decrease = min(changes)
    m2 = int(changes.index(max_decrease)) +1
    month2 = dates[m2]

    print("\nGreatest increase in Profits: ", month1, "  ($", int(max_increase), ")")
    print("\nGreatest decrease in Profits: ", month2, "  ($", int(max_decrease), ")\n")


file_out = open(r'C:\Users\ramir\python\python-challenge\PyBank\analysis\PyBank.txt', 'w')
file_out.write("\nFinancial Analysis\n \n-----------------------------\n ")

file_out.write(f'\nTotal Months: {months}\n')
file_out.write(f'\nAverage Change: ${"%.2f" % float(avg)}\n')
file_out.write(f'\nGreatest increase in Profits: {month1}  (${int(max_increase)})\n')
file_out.write(f'\nGreatest decrease in Profits: {month2}  (${int(max_decrease)})\n') 
    
file_out.close()
