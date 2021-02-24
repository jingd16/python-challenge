import os
import csv

#Set path to read and write CSV file
csvpath = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("analysis", "PyPoll.txt")

Total_vote = 0
Newlist =[]
Newlist2=[]
voterID_List = []
Location_List = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Skip the header
    csv_header = next(csvreader)

    #Loop through the CSV file to: 
    #   1. Count how many rows/vote in total
    #   2. Create a list for each column in CSV file, and add the list while looping through all the rows
    for row in csvreader:
        #Count total Votes from total line of rows
        Total_vote = Total_vote + 1
        
        #add each value into a list
        candidate_name = str(row[2])
        voterID = str(row[0])
        location = str(row[1])
        Newlist.append(candidate_name)
        voterID_List.append(voterID)
        Location_List.append(location)  

#Print Headline of the summary
print("Election Results")
print("---------------------")

#Print total vote
print("Total Votes: " + str(Total_vote))
print("---------------------")

#Create a new Candidate list, but delete all repeatitive values/names
Newlist2=list(set(Newlist)) 

#Count the new candidiate list, and find out how many candidates are there, so we can setup how many times we need to loop through the dataset
count_Loop = len(Newlist2)

name_of_Candidate = ""
Candidiate_Vote_Count = 0
winner = ""
winner_count = 0

#Create a list of results, so we can write the information into a CSV file later. 
Results_List=[]

#Now we know how many candidates in total, setup a loop to go through the dataset x amount of times, to add up votes for that candidate
for x in range(0, count_Loop):
    #Create a turple by zipping all the collumns/lists
    #---Check with TA/Manager--- 
    # How to ask the pointer to go to the top of the turple when completing multiple loop. Tried to define the pollData(Turple) outside the loop, so it's more efficient, but it will only provide information for first candidiates.
    pollData = zip(voterID_List, Location_List, Newlist)
    name_of_Candidate = Newlist2[x]
    
    #Reset vote count for each candidate
    Candidiate_Vote_Count = 0

    #looping through the turple according to the candidate name, and add up votes for Each candidates.
    for y in pollData:
        if y[2] == name_of_Candidate:
            Candidiate_Vote_Count = Candidiate_Vote_Count + 1
    per_vote = round((Candidiate_Vote_Count / Total_vote) * 100, 0)
    
    #Print results + Save the result to a list to write a text file later
    print(name_of_Candidate + ": " + str(per_vote) +"%  (" + str(Candidiate_Vote_Count) + ") ")
    Results_List.append(name_of_Candidate + ": " + str(per_vote) +"%  (" + str(Candidiate_Vote_Count) + ") ")
    
    #Compare the vote result and find the person with highest count, then print the winner name
    if per_vote > winner_count:
        winner_count = per_vote
        winner = name_of_Candidate

print("---------------------")    
print ("Winner: " + winner)
print("---------------------")

#write the summary information to a text file
with open(output_file, "w") as outputFile:
    csvwriter = csv.writer(outputFile)

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["------------------------------"])
    csvwriter.writerow(["Total Votes: " + str(Total_vote)])
    csvwriter.writerow(["------------------------------"])
    
    for row in Results_List:
        csvwriter.writerow([row])

    csvwriter.writerow(["------------------------------"])
    csvwriter.writerow(["Winner: " + winner])
    csvwriter.writerow(["------------------------------"])