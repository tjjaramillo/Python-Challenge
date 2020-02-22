# Import needed functions to read csv file
import os
import csv

# Path to csv file containing election data
Election_Data = os.path.join("Resources", "Election_Data.csv")

# Create empty lists in which we will populate candidate names, their votes, and the percentage
# of their votes from the total amount. 

Candidates = []
Vote_Count = []
Vote_Percentage = []

# Start total votes at zero

Total_Vote_Count = 0


# Open and read csv file

with open(Election_Data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)


    for row in csvreader:

        # Start loop with adding a vote to the total vote count

        Total_Vote_Count += 1

        # If candidate name is not in the existing list of candidates, add them to the list and put a 
        # vote with their name

        if row[0] not in Candidates:
            Candidates.append(row[0])
            Vote_Count.append(1)

        #If candidate name is in the existing list of candidates, add a vote to their name with their existing index

        else:
            candidate_index = Candidates.index(row[0])
            Vote_Count[candidate_index] += 1

    # Take vote percentage of each candidate from the total amount of votes
    
    for vote in Vote_Count:
        percentage = (vote/Total_Vote_Count)
        percentage = round(percentage)
        percentage = format(percentage, ".2%")
        Vote_Percentage.append(percentage)

    # Capture the winning candidate with the highest vote count

    Winning_Candidate = max(Vote_Count)
    index = Vote_Count.index(Winning_Candidate)
    Winning_Candidate = Candidates[index]

# Printed election results
print("Election Results")
print("-----------------------------")
print("Total Votes: " + str(Total_Vote_Count))
print("----------------------------")
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {str(Vote_Percentage[i])})")
print("----------------------------")
print(f"Winner: {Winning_Candidate}")
print("----------------------------")
