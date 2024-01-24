import csv
import os

csvpath = os.path.join("/Users/kyle.tavtener/Desktop/UPENN-VIRT-DATA-PT-12-2023-U-LOLC/02-Homework/03-Python/Starter_code/PyPoll/Resources/election_data.csv")

#Declaring known variables
TotalVotes = 0 
candidate_votes = {'Charles Casper Stockham': 0, 'Diana DeGette': 0, 'Raymon Anthony Doane': 0}
Winner = ""

#Opening and reading the csv file
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)    

    for row in csvreader:
        candidate = row[2].strip()  
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
            TotalVotes += 1

# Determining the winner based on number of votes received 
max_votes = max(candidate_votes.values())
winners = [candidate for candidate, votes in candidate_votes.items() if votes == max_votes]
Winner = winners[0] if len(winners) == 1 else "Tie"

# Printing out results in a file
output_file = "/Users/kyle.tavtener/Desktop/result.txt"
with open(output_file, "w") as results: 
    results.write("Election Results\n")
    results.write("----------------------------\n")
    results.write(f"Total Votes: {TotalVotes}\n")
    results.write("----------------------------\n")

    for candidate, votes in candidate_votes.items():
        percentage = (votes / TotalVotes) * 100 if TotalVotes > 0 else 0
        results.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    
    results.write("----------------------------\n")
    results.write(f"Winner: {Winner}\n")
    results.write("----------------------------\n")