# Module 3 Python Challenge
## PyPoll exercise


import os
import csv

electiondata_csv = r"C:\Users\ramir\python\Resources\election_data.csv"
voterids = []
candidates = []

# Open and read csv
with open(electiondata_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)
    

    for row in csvreader:
        voterids.append(row[0])
        candidates.append(row[2])
        
    votes = len(voterids)

print("\nElection Results\n \n-----------------------------\n ")    
print("Total Votes: ", votes)
print("\n-----------------------------\n ")

new_candidates = []
new_votes = []
percent = 0
new_percent = []

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



file_out = open(r'C:\Users\ramir\python\python-challenge\PyPoll\analysis\PyPoll.txt', 'w')
file_out.write("\nElection Results\n \n-----------------------------\n ")
file_out.write(f'\nTotal Votes: (votes)\n \n-----------------------------\n')


combos = sorted(zip(new_candidates,new_percent,new_votes))

for item in combos:
    print(item[0],": ",item[1],"%  (",item[2],")\n")
    file_out.write(f'{item[0]} : {item[1]}%  ({item[2]})\n')


winner = max(new_votes)
i = int(new_votes.index(winner))
print(f'-----------------------------\n \nWinner: {new_candidates[i]} \n \n-----------------------------\n')


file_out.write(f'\n-----------------------------\n \nWinner: {new_candidates[i]} \n-----------------------------\n')   
file_out.close()