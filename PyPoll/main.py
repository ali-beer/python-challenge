# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

# As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```
 
 
# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Create lists
votes = []
candidates = []
candidate_unique = []
total_votes = 0
candidate_dict = {}

# Open the CSV
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (stores the line that it skips)
    csv_header = next(csvreader)

    # Read each row of data (everything 1 indent in from here is in the for loop)
    for row in csvreader:       

        # Add candidate rows to list
        candidates.append(row[2])

        # Add voter ID rows to votes list
        votes.append(row[0])

        total_votes = total_votes + 1

        if row[2] in candidate_dict:
            candidate_dict[row[2]] += 1
        else:
            candidate_dict[row[2]] = 1 

print(candidate_dict)
count_votes = (len(votes))
# print(count_votes)

# print(total_votes)

unique_candidates = set(candidates)

print(candidate_dict.keys())

for candidate in candidate_dict.keys(): # looping through list and get the value for each key
    # .keys function gives a list of the keys within a dict). Prints result and then goes back and starts again. If print outside 
    # of loop would only print the last loop.
    
    percent = candidate_dict[candidate] / total_votes

    print(f'{candidate}: {round(percent, 3)}% ({candidate_dict[candidate]})')

# print(f'{candidate_dict[candidate]})

# print(unique_candidates)

# candidate_votes = {}

# for i in candidates:
#     if i in candidate_votes:
#         candidate_votes[i] += 1
#     else:
#         candidate_votes[i] = 1


# print(f'{candidate_dict[khan] }')

# print(candidate_votes)

# print(f'{candidate_votes}')

# for key, value in candidate_votes():
#     percent[key] = round((value/total_votes)*100,2)

# for key in candidates.keys():
#     if candidates[key] > winner_count:
#         winner = key
#         winner_count = candidates[key]



# The total votes
# print(f'Total votes: {total_votes}')

# The list of candidates and number of votes received
# print(candidate_count)
    
# The percentage of votes each candidate won
# print(percent)

# The winner of the election based on popular vote.
# print(f'Winner: {winner}')


# In addition, your final script should both print the analysis to the terminal and export a text file with the results.