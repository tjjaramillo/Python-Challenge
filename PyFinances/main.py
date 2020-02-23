# Import dependencies
import os
import csv

# Set file path to csv file
file_path = os.path.join("Budget_Data.csv")

# Start totals at zero and set empty lists for dates and profits/losses
Total_Months = 0
Total_PL = 0
Value = 0
Change = 0
Dates = []
Profits = []

with open(file_path) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    
    #Read the first row so we are able to track changes properly
    first_row = next(csvreader)
    Total_Months += 1
    Total_PL += int(first_row[0])
    Value = int(first_row[0])
    
    #Go through each row of data after the header & first row 
    for row in csvreader:
        # Keep track of all dates
        Dates.append(row[1])
        
        # Calculate the change, then add it to list of changes
        Change = int(row[0])-Value
        Profits.append(Change)
        Value = int(row[0])
        
        #Total number of months
        Total_Months += 1

        #Total net amount of "Profit/Losses over entire period"
        Total_PL = Total_PL + int(row[0])

    #Greatest increase in profits
    greatest_increase = max(Profits)
    greatest_index = Profits.index(greatest_increase)
    greatest_date = Dates[greatest_index]

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(Profits)
    worst_index = Profits.index(greatest_decrease)
    worst_date = Dates[worst_index]

    #Average change in profits/losses over all months in data
    average_change = sum(Profits)/len(Profits)
    

#Print out financial analysis
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(Total_Months)}")
print(f"Total: ${str(Total_PL)}")
print(f"Average Change: ${str(round(average_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")