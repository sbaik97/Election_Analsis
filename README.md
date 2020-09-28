# Election_Analsis #

Election Analysis by using Python programming language


### Project Background ###
The purpose of this phython secript is analysising the election data for the following tasks to complete the election audit of a recent local congressional election in Colorado.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

The other task is analysing the voter turnout for each county with following tasks,
1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

### SOFTWARE/TOOLS/LIBRARIES ###
Python 3.7.6, Visual Studio Code, 1.49.2

Data Source: election_results.csv

## Results ##

The analysis of the candidate vote show that:

1. There were 369,711 votes cast in the election.
2. The candidates were: + Charles Casper Stockham, + Diana DeGette, + Raymon Anthony Doane
3. The total numbers of vote each candidate received were:
   + Charles Casper Stockham has recieved 85213 votes. 
   + Diana DeGette has recieved 272892 votes. 
   + Raymon Anthony Doane has recieved 11606 votes.
4. The percentages were:
   + 23.0% of the vote for Charles Casper Stockham.
   + 73.8% of the vote for Diana DeGette.
   + 3.1% of the vote for Raymon Anthony.
5. The winner of the election was: Diana DeGette received 73.8% of the vote and (272,892) number of votes.

The results of python script for election analysis are following,
  
![](/Image_of_Candidate_analysis.PNG)


The analysis of the the voter turnout for each county and candidate vote shows that:

1. There were 369,711 votes cast in the election.
2. The county involed for elction were: Jefferson, Denver, and Arapahoe in Colorado.
3. The voter turnout for each county were:
   + The Jefferson county has 38,855 votes. 
   + The Denver county has 306,055 votes. 
   + The Arapahoe county has 24,801 votes.
4. The vote turnout were:
   + 10.5% for the Jefferson county.
   + 82.8% for the Denver county.
   + 6.7% % for the Arapahoe county.
5. The largest county turnout was: Denver has turnout of 82.8% with (306,055) number of votes.

The resuls of python script for the voter turnout for each county are following,

 ![](/Image_of_County_and_Candidate_Analysis.PNG)



## Conclusions

From this Python practice, we've learn how to analysis the csv file using the data structures like lists, tuples, and dictionaries. We also created the decision and repetition statements using the Boolean and For loop to evaluate the vote election analysis.

Finally, we can calculate the total number of votes cast, get a  list of candidates and counties and their vote counts, finally fetermine the winner of the election and county that had the largest turnout.


## Program Logical Flow

Using repetition statements, conditional statements with logical operators, and print statements, we analysis the candidate and county election results.

1a. Add dependenciess and variables to load and save a file from a path. 
```
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_results_for_county.txt")
```
1b. Initialized a total vote counter and county and candidate_option list and county and candidate votes.
```
# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}
```
1c. Initialize a county_dictionary and candidate_votes dictionary, that will hold 
the county and candidate as the key and the votes cast for each county as the values.
```
county_list = []
county_votes = {}
```
2a. Initialize an empty string of winning_candidate and winning_county, that will hold the
candidate and county name that have the largest turnout.
Initialize a winning_count and winning_county_count variables, that will hold the
number of votes of the candidate and county that had the largest turnout.
```
# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county and county voter turnout.
winning_county = ""
winning_county_count = 0
winning_county_turnout = 0

```
3. Get the county name from each row while reading the election results from each row inside the for loop,
```
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:

    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]
        # 3: Extract the county name from each row.
        county_name = row[1]
        
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        
```

4. Write a decision statement that checks that the county does not match any existing county in the county list and add the existing county to the list of counties, initialize the tracking the county's vote count.
```
   
        if county_name not in county_list:

            county_list.append(county_name)

            county_votes[county_name] = 0

```
5. Adds a vote to the county’s vote count as you are looping through all the rows and print and save the final vote count.
```
        county_votes[county_name] += 1 
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------------\n"
        f"County Results:\n\n")
        
    print(election_results, end="")

    txt_file.write(election_results)
```
6a. Write a repetition statement to get the county from the county dictionary and initialize a variable to hold the county’s votes as they are retrieved from the county votes dictionary, get a  percentage of county’s votes from the total votes, finallym prints the current county, its percentage of the total votes, and its total votes to the command line.
```
    for county_name in county_votes:
            
        votes = county_votes[county_name]

        vote_percentage = float(votes) / float(total_votes) * 100

        county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
        print(county_results)
        
        txt_file.write(county_results)

```

6f: Write a decision statement to determine the winning county and get its vote count.
```
        if (votes > winning_county_count) and (vote_percentage > winning_county_turnout):
            winning_county_count = votes
            winning_county_turnout = vote_percentage
            winning_county = county_name
```      
7. Prints out and save the county with the largest turnout to a text file
```
    winning_county_summary = (f"----------------------------------\n"
            f"Largest County Turnout: {winning_county}: {winning_county_turnout:.1f}% ({winning_county_count:,})\n"
            f"---------------------------------------------------\n"
            f"Candidate Results:\n")
    print(winning_county_summary)
    
    txt_file.write(winning_county_summary)
```
8. Get  candidate's vote count and percentage and determine the final winner of election. 
```
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.

        txt_file.write(candidate_results)

                
# Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    
        winning_candidate_summary = (
        f"----------------------------------\n"
        f"Winning Candidate Summary\n\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------------------------------\n")
    print(winning_candidate_summary)

# Save the winning candidate's name to the text file

    txt_file.write(winning_candidate_summary)
```




