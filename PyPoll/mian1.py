import os
import csv

pollData = os.path.join(".","Resources","election_data.csv")
#currentDirectory = os.getcwd()
#print(currentDirectory)
#print(pollData)

# Open the CSV file
with open(pollData, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

  # The total number of votes cast (row count after the header)
    next(csvreader)
    data = list(csvreader)
    row_count = len(data)

  # Create new list from CSV column "C" to get a complete list of candidates who received votes
    candilist = list()
    tally = list()
    for i in range (0,row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candilist: 
            candilist.append(candidate)
    candicount = len(candilist)

  # The total number of votes each candidate won & the percentage of votes each candidate won
    votes = list()
    percentage = list()
    for j in range (0,candicount):
        name = candilist[j]
        votes.append(tally.count(name))
        vprct = votes[j]/row_count
        percentage.append(vprct)

  # The winner of the election based on popular vote.
    winner = votes.index(max(votes))    

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
  # Print the results to terminal
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------------------")
    for k in range (0,candicount): 
        print(f"{candilist[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {candilist[winner]}")
    print("----------------------------")

  # Print the results to "PyPoll.txt" file
    print("Election Results", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Total Votes: {row_count:,}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    for k in range (0,candicount): 
        print(f"{candilist[k]}: {percentage[k]:.3%} ({votes[k]:,})", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Winner: {candilist[winner]}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))