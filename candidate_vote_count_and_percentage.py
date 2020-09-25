##In this project, our final Python script will need to be able to deliver the following information when the script is run: 

1.Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. Save the results to our text file
6. The winner of the election based on popular vote
##

## 1. Get the Total Votes from election_results.csv.

# Add dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # REad the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:
            #2. Add to the totla vote count.
            total_votes += 1
            
# Print the totla votes.
print(total_votes)

# resutls: 369711


## 2. Get the list of candidates who received votes


import csv
import os
# Assign a variable to load a file from a path and to save the file to a path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

Initialial vote count.
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)

# resutls: ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']


## 3. Get the total number of votes each candidate received

import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
fiel_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

candidate_options = []

candidate_votes= {}

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    header = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name] =  0
            
        candidate_votes[candidate_name] += 1

print(candidate_votes)   

# resutls: {'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}


## 4. Get the percentage of votes each candidate won

# Add our dependencies.

#Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
#Creaste a list for both Candidate and County.
candidate_options = []
county_options = []
#Create empty dictionaries for Candidate and County.
candidate_votes = {}
county_votes = {}

# Winning Candidate & County and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.To ensure it would skip this row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:
          # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#5.Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
    # Save the final vote count to the text file.
        ##txt_file.write(election_results)
        #Election Results
#-------------------------
#Total Votes: 369,711
#-------------------------
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.

        for candidate_name in candidate_votes:
            # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # Print the candidate vote dictionary.

            # 3. Calculate the percentage of votes.      
            vote_percentage = float(votes) / float(total_votes) * 100

            # 4. Print the candidate name, percentage, and votes of votes.
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            #result Charles Casper Stockham: 23.0% (85,213)
            #Diana DeGette: 73.8% (272,892)
            #Raymon Anthony Doane: 3.1% (11,606)
            
            # 5. Save the candidate results to our text file.
            txt_file.write(candidate_results)
            
#6. Determine winning vote count, winning percentage, and winning candidate.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
        winning_candidate_summary = (f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        # Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)
#results
#-------------------------
#Winner: Diana DeGette
#Winning Vote Count: 272,892
#Winning Percentage: 73.8%
#-------------------------






