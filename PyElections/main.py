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

with open(Election_Data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)


    for row in csvreader:

        Total_Vote_Count += 1

        if row[0] not in Candidates:
            Candidates.append(row[0])
            Vote_Count.append(1)

        else:
            candidate_index = Candidates.index(row[0])
            Vote_Count[candidate_index] += 1

    

    for vote in Vote_Count:
        percentage = (vote/Total_Vote_Count)
        percentage = round(percentage)
        percentage = format(percentage, ".2%")
        Vote_Percentage.append(percentage)

    Winning_Candidate = max(Vote_Count)
    index = Vote_Count.index(Winning_Candidate)
    Winning_Candidate = Candidates[index]

print(str(Total_Vote_Count))

