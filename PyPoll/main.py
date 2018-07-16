# PyPoll Homework Rose Wachira
#import modules
import csv
import os

# set the path of the file
csvpath = os.path.join('Resources', 'election_data.csv') 

#variables
votes_cast = 0
Candidates = {}
Candidates_percent = {}
election_winner = ""
election_winnerCount = 0

#open the file
with open(csvpath,newline = "")as csvfile:
    csv_reader=csv.reader(csvfile, delimiter = ",")
    next(csv_reader,None)
    
#Formula to find each candidates votes and total of votes cast    
    for row in csv_reader:
        votes_cast += 1
        if row[2] in Candidates.keys():
            Candidates[row[2]] += 1
        else:
            Candidates[row[2]] = 1
#print(votes_cast) 
  
#calculating percentage for each canditate
for key, value in Candidates.items():
    Candidates_percent[key] = round((value/votes_cast)*100,2)
#print(Candidates_percent) 

#Identifying the winner in elections
for key in Candidates.keys():
    if Candidates[key]> election_winnerCount:
        winner = key
        election_winnerCount = Candidates[key]
#print(winner)  


#print script
print("Election Results")
print("------------------------------------------")
print("Total Votes:" + str(votes_cast))
print("------------------------------------------")
print(key + ":" + str(Candidates_percent[key]) + "%(" + str(value) +")")
print("-------------------------------------------")
print("Winner:" + winner)
print("-------------------------------------------")

#Text File
PyPoll = open("poll_results.txt","w")

#Writing PyPoll Text File
PyPoll.write("Election Results \n")
PyPoll.write("------------------------\n")
PyPoll.write("Total Votes:" + str(votes_cast) + "\n")
PyPoll.write("-------------------------\n")
for key, value in Candidates.items():
    PyPoll.write(key + ":" + str(Candidates_percent[key]) +"%(" + str(value)+ ")\n")
PyPoll.write("--------------------------\n")
PyPoll.write("Winner:" + winner + "\n")
PyPoll.write("--------------------------\n")