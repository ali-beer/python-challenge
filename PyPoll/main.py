## PyPoll
# Import os module and modeule for reading csv files
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Create variables to store data
total_votes = 0
candidate_dict = {}
results_list = []

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (stores the line that it skips)
    csv_header = next(csvreader)

    # Read each row of data (everything 1 indent in from here is in the for loop)
    for row in csvreader:
        total_votes = total_votes + 1

        # If the candidate in row[2] of the csv file is in candidate dict
        # add 1 to the candidate key value in dict, else key value equal to 1
        if row[2] in candidate_dict:
            candidate_dict[row[2]] += 1
        else:
            candidate_dict[row[2]] = 1

# Loop through list and get the value for each key
# The .keys() function gives a list of the keys within a dict
for candidate in candidate_dict.keys():
    percent = (candidate_dict[candidate] / total_votes)*100
    
    # Append the result to a list
    results_list.append(f'{candidate}: {round(percent, 3)}% ({candidate_dict[candidate]})')

# Get winner of the election based on popular vote and print result
winner = max(candidate_dict, key=candidate_dict.get)

# Print results
print("Election Results")
print("---------------------")
print(f'Total votes: {total_votes}')
print("---------------------")
for i in results_list:
    print(i)
print("---------------------")
print(f'Winner: {winner}')
print("---------------------")

# Write results to a text file
f = open("Analysis/Output.txt", "w")
f.write('Election Results\n')
f.write('---------------------------------------\n')
f.write(f'Total votes: {total_votes}\n')
f.write('---------------------------------------\n')
for i in results_list:
    f.write(f'{i}\n')
f.write('---------------------------------------\n')
f.write(f'Winner: {winner}\n')
f.write('---------------------------------------\n')   
f.close()

  