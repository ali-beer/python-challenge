#  ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# Cntr s - to save

# Import os module and module for reading CSV files
import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

# Create lists to store data
date = []
profit_losses = []

# Create variable to store total amount
amount = 0

# Open and read csv
with open(csvpath) as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (stores the line that it skips)
    csv_header = next(csv_reader)

    # Read each row of data (everything 1 indent in from here is in the for loop)
    for row in csv_reader:       
    
        # Add row to month list
        date.append(row[0])
        
        # Add Profit/Losses to list
        profit_losses.append(int(row[1]))
        
        # Add Profit/Losses to amount
        amount += int(row[1])

# The total months
month_count = (len(date))

print(f'Total months: {month_count}')
print(f'Total: ${amount}')

# List to store the changes in "Profit/Losses" over the entire period and date
profit_losses_change = []

# Enumerate allows you to keep track of index and item itself whereas a for loop keeps track of item only. 
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

print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {date_max_increase} (${max_increase})')
print(f'Greatest Decrease in Profits: {date_max_decrease} (${max_decrease})')

# Export a text file with the results
with open("Analysis/Output.txt", "w") as text_file:
    print('Financial Analysis', file=text_file)
    print('--------------------------------------------------', file=text_file)
    print(f'Total months: {month_count}', file=text_file)
    print(f'Total: ${amount}', file=text_file)
    print(f'Average Change: ${average_change}', file=text_file)
    print(f'Greatest Increase in Profits: {date_max_increase} (${max_increase})', file=text_file)
    print(f'Greatest Decrease in Profits: {date_max_decrease} (${max_decrease})', file=text_file)






# Loop through number of items in profit_losses list
# for i in range(len(profit_losses)):  
    
#     # Get the change amount from row before to current row
#     if i > 0:
#         change = profit_losses[i] - profit_losses[i-1]

#         # Append change amounts to list
#         profit_losses_change.append(change)

# print(profit_losses_change)
# average_change = sum(profit_losses_change) / len(profit_losses_change)
# print(average_change)


