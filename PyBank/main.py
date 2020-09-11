## PyBank
# Import os module and module for reading CSV files
import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

# Create variables to store data
date = []
profit_losses = []
amount = 0

# Open and read csv
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (stores the line that it skips)
    csv_header = next(csv_reader)

    # Read each row of data (everything 1 indent in from here is in the for loop)
    for row in csv_reader:       
    
        # Add date to month list
        date.append(row[0])
        
        # Add profit/losses to list
        profit_losses.append(int(row[1]))
        
        # Add Profit/Losses to amount variable
        amount += int(row[1])

# The total months
month_count = (len(date))

# Create List to store the changes in "Profit/Losses" over the entire period
profit_losses_change = []

# Enumerate allows you to keep track of index and item itself whereas a 'for loop' keeps track of item only. 
# Note: If range of length is 10, -1 is telling it to only loop 9 times
for i, item in enumerate(range(len(profit_losses)-1)): 
    change = (profit_losses[i+1] - profit_losses[i])
    profit_losses_change.append(change)

# The average change
average_change = round(sum(profit_losses_change) / len(profit_losses_change), 2)

# The greatest increase and decrease in profits (date and amount) over the entire period
max_increase = max(profit_losses_change)
max_decrease = min(profit_losses_change)

# Locate the index value of greatest increase and decrease in profits
max_increase_index = profit_losses_change.index(max_increase)
max_decrease_index = profit_losses_change.index(max_decrease)

# Obtain the date associated with greatest increase and decrease
date_max_increase = date[profit_losses_change.index(max_increase)+1]
date_max_decrease = date[profit_losses_change.index(max_decrease)+1]

# Print results
print("Financial Analysis")
print('----------------------------------------------')
print(f'Total months: {month_count}')
print(f'Total: ${amount}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {date_max_increase} (${max_increase})')
print(f'Greatest Decrease in Profits: {date_max_decrease} (${max_decrease})')

# Write results to text file
f = open("Analysis/Output.txt", "w")
f.write('Financial Analysis\n')
f.write('--------------------------------------------------\n')
f.write(f'Total months: {month_count}\n')
f.write(f'Total: ${amount}\n')
f.write(f'Average Change: ${average_change}\n')
f.write(f'Greatest Increase in Profits: {date_max_increase} (${max_increase})\n')
f.write(f'Greatest Decrease in Profits: {date_max_decrease} (${max_decrease})\n')
f.close()
