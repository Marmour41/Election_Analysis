#The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize vote counter
total_votes = 0

#List of candidates
candidate_options = []

#Candidate and their votes
candidate_votes = {}

#Winning candidate and winning count tracjer
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results ad read the file.
with open(file_to_load) as election_data:

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    for row in file_reader:

        #Add to the total vote count
        total_votes +=1

        #Add the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #Begin tracking candidate vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    #Save the results to our text file
    with open(file_to_save, "w") as txt_file:

        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        #Determine the percentage of votes for each candidate by looping through the candidate options
        #iterate through the candidate list
        for candidate_name in candidate_votes:

            #retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]

            #calculate percentage of votes
            vote_percentage = float(votes) / float(total_votes) * 100

            if (votes > winning_count) and (vote_percentage > winning_percentage):

                #if true then set winning_count = votes and winning_percent = vote percentage
                winning_count = votes
                winning_percentage = vote_percentage

                #set the winning_candidate equal to the candidate name
                winning_candidate = candidate_name


            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

        winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")
        
        txt_file.write(winning_candidate_summary)







   

