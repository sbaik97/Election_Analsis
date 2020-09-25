"""In this project, our final Python script will need to be able to deliver the following information when the script is run: 

1. Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. The winner of the election based on popular vote
6. Save the results to our text file"""

## 1. Get the Total Votes from election_results.csv.

# Add dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis_for_candidate.txt")

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
    fstring_total_vote = (
        f"\nTask#1 Result\n"
        f"------------------------------------\n"
        f"Total number of votes cast is {total_votes}\n"
        f"------------------------------------\n")
    
# Print the totla votes.
print(fstring_total_vote)

with open(file_to_save, "w") as txt_file:
    # Save the final vote count to the text file.
    txt_file.write(fstring_total_vote)
        
        
#resutls: Total number of votes cast is 369711


## 2. Get the list of candidates who received votes

import csv
import os
# Assign a variable to load a file from a path and to save the file to a path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis_for_candidate.txt")

#Initialial vote count.
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
            
    fstring_candiate_list = (
        f"\nTask#2 Result\n"
        f"------------------------------------\n"
        f"The list of candidates who received votes is \n" 
        f"{candidate_options}\n"
        f"------------------------------------\n")
    
# Print the candidate list.
print(fstring_candiate_list)

with open(file_to_save, "a") as txt_file:
    # Save the final vote count to the text file.
    txt_file.write(fstring_candiate_list)
        
        
#resutls: The list of candidates who received votes are ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
           
      
"""resutls: ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']"""


## 3. Get the total number of votes each candidate received

import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
fiel_to_save = os.path.join("analysis", "election_analysis_for_candidate.txt")

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

    fstring_candidate_votes = (
        f"\nTask#3 Result\n"
        f"------------------------------------\n"
        f"The total number of votes each candidate received is \n" 
        f"{candidate_votes}\n"
        f"------------------------------------\n")
    
# Print the candidate list.
print(fstring_candidate_votes)

with open(file_to_save, "a") as txt_file:
    # Save the final vote count to the text file.
    txt_file.write(fstring_candidate_votes)        
        
        
#resutls:The total number of votes each candidate received are {'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}




## 4. Get the percentage of votes each candidate won

# Add our dependencies.

import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis_for_candidate.txt")

# 1. Initialize a total vote counter.
total_votes = 0
#Creaste a list for both Candidate and County.
candidate_options = []
county_options = []
candidate_votes = {}
county_votes = {}

# Winning Candidate & County and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


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

    with open(file_to_save, "a") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        
#        print(election_results, end="")
    # Save the final vote count to the text file.
#        txt_file.write(election_results)
        
# Determine "f" by looping through the counts.
        # 1. Iterate through the candidate list.
    
        vote_percentage_dict = {}
        for candidate_name in candidate_votes:
            # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # Print the candidate vote dictionary.

            # 3. Calculate the percentage of votes.      
            vote_percentage = float(votes) / float(total_votes)*100
            
            # 4. Add the candidate name and percentage of votes.
            vote_percentage_dict[candidate_name] = round(vote_percentage,1)
       
        candidate_results = (
                        f"\nTask#4 Result\n"
                        f"------------------------------------\n"
                        f"The percentage of votes each candidate won is \n" 
                        f"{vote_percentage_dict}\n")
            
        print(candidate_results)

        
        #result:The percentage of votes each candidate won is {'Charles Casper Stockham': 23.0, 'Diana DeGette': 73.8, 'Raymon Anthony Doane': 3.1}

            
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
        
        
#5. Determine winning vote count, winning percentage, and winning candidate.

if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
    winning_count = votes
    winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
    winning_candidate = candidate_name
    winning_candidate_summary = (
            f"\nTask#5 Result\n"
            f"------------------------------------\n"
            f"winning_candidate_summary\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
    print(winning_candidate_summary)
    
    
    
# 6. Save the candidate results to our text file.    
    with open(file_to_save, "a") as txt_file:
        txt_file.write(winning_candidate_summary)
  


# Results:
#winning_candidate_summary
#Winner: Raymon Anthony Doane
#Winning Vote Count: 11,606
#Winning Percentage: 3.1%







