print('Hello World')
my_dictionary = {}
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
len(counties_dict)
counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.get("Denver")
counties_dict['Arapahoe']
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters":422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 4324438})
voting_data
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I recievied " + str(percentage_votes)+"% of the totals votes.")
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
temperature = int(input("What is the temperature outside? "))
if temperature > 80:
    print("Turn on the AC. ")
else:
    print("Open the windows. ")
score = int(input("What is your test score? "))
if score >= 90:
    print('Your grade is an A. ')
else:
    if score >= 80:
        print('Your grade is a B. ')
    else:
        if score >= 70:
            print('Your grade is a C ')
        else:
            if score >= 60:
                print('Your grade is a D ')
            else:
                print('Your grade is an F. ')
#or
if score >= 90:
    print('Your grade is an A. ')
elif score >= 80:
    #etc...
    #end with
    else:
        print('Your grade is an F. ')
x = 0
while x <= 5:
    print(x)
    x = x + 1
for county in counties:
    print(county)
for i in range(len(counties)):
    print(counties[i])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
# for key, value in dictionary_name.items():
    #print(key, value)
for county, voters in counties_dict,items():
    print(county, voters)
voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
#3.2.11
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100"}% of the total votes. ")
counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters. ")
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters. ")
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of botes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes,}. "
    f"You recieved {candidate_votes / total_votes * 100: .2f}% of the total votes. ")
print(message_to_candidate)
