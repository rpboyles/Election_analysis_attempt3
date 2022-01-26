# Election_analysis_attempt3
# import the ability to use CSV files
import csv
# import os
import os
# assigning a variable for the file to load
file_to_load = os.path.join("Resources", "election_results.csv")
# assigning a variable for the file to save
file_to_save = os.path.join("analysis", "election_analysis,txt")
# total votes variable
total_votes = 0
# candidate options empty list
candidate_options = []
# candidate votes emmpty dictionary
candidate_votes = {}
# winning candidate empty variable
winning_candidate = ""
# variable to count the number for winning votes
winning_count = 0
# variable to get the winning percentage of votes
winning_percentage = 0
# reading a file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
# set up of text file
    headers = next(file_reader)

    for row in file_reader:
        total_votes += 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:
# adding unkown candidates that received votes
            candidate_options.append(candidate_name)
# votes per candidate
        candidate_votes[candidate_name] = 0
# adding a vote
    candidate_votes[candidate_name] += 1
# output to texr file
with open(file_to_save, "w") as txt_file:
# the printable results
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total_votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end= "")

    txt_file.write(election_results)
# the work
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

        print(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_percentage}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage: 1f}%\n"
        f"--------------------------\n")

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)
    
# We were tasked with making since of the election data after a vote
# We created the code above with its # notes.
# We needed to read, write and save files.
# We found the winners and losers, with their total votes as well as the percentage of votes they recieved.
