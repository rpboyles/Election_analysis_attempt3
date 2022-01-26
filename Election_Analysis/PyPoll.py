
# the data we need to retieve.
# 1. the total number of votes cast
# 2. a complete list of candidates who received bots
# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the winner of the election based on popular vote
import datetime as dt
now = dt.datetime.now()
print("The time right now is ", now)

#file_to_load = 'Resources/election_results.csv'
#election_data = open(file_to_load, 'r')

#election_data.close()

#with open(file_to_load) as election_data:
#    print(election_data)
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    print(election_data)
#file_to_save = os.path.join("analysis", "election_analysis.txt")
#open(file_to_save, "w")
