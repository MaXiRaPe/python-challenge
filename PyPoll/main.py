# Module 3 Python Challenge
## PyPoll exercise


import os
import csv

## Create a variable to call your data source
electiondata_csv = r"C:\Users\ramir\python\Resources\election_data.csv"
## Define list variables for processing the data of interest
voterids = []
candidates = []

# Open and read csv
with open(electiondata_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)
    
## Fill in the list variables with the data from the csv file
    for row in csvreader:
        voterids.append(row[0])
        candidates.append(row[2])
## Use the lenght of the length of the "ballot id" column as a counter        
    votes = len(voterids)

print("\nElection Results\n \n-----------------------------\n ")    
print("Total Votes: ", votes)
print("\n-----------------------------\n ")
## create new list variables to transform the summarize the date
new_candidates = []
new_votes = []
percent = 0
new_percent = []
## Use the 'set' function to identify the list of individual candidates and use this to validate 
## the multiple entries and create the new lists with the candidate names and their corresponding total votes
## Use the new set of total vote count to calculate each candidates percentage of the total votes
for new in set(candidates):
    tot_votes = 0
    for candidate in candidates:
        if candidate == new:
            tot_votes += 1
    new_votes.append(tot_votes)
    new_candidates.append(new)
for count in new_votes:
    percent = count/votes*100
    new_percent.append("%.3f" % percent)


## Create a txt file using 'open', 'w' and 'write'
file_out = open(r'C:\Users\ramir\python\python-challenge\PyPoll\analysis\PyPoll.txt', 'w')
file_out.write("\nElection Results\n \n-----------------------------\n ")
file_out.write(f'\nTotal Votes: (votes)\n \n-----------------------------\n')

## Used the 'zip' function to combine the three lists into a list of tuples
## Use the 'sorted' funtion to sort the information in ascending order based on the first tuple
## Used a variable to store the transformed data to ensure the print-out would remain in the same order
combos = sorted(zip(new_candidates,new_percent,new_votes))
## Used a loop to printout and write to the text
for item in combos:
    print(item[0],": ",item[1],"%  (",item[2],")\n")
    file_out.write(f'{item[0]} : {item[1]}%  ({item[2]})\n')

## Used the 'max' and 'index' functions to find the winning candidate with the maxmum of votes
winner = max(new_votes)
i = int(new_votes.index(winner))
print(f'-----------------------------\n \nWinner: {new_candidates[i]} \n \n-----------------------------\n')


file_out.write(f'\n-----------------------------\n \nWinner: {new_candidates[i]} \n-----------------------------\n')   
file_out.close()
