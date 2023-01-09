import os
import csv
election_data = os.path.join("election_data.csv")
with open("election_data.csv", newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
        
    candidate_list = [candidate[2] for candidate in csvreader]

total_votes = len(candidate_list)   
candidates_name = [[candidate,candidate_list.count(candidate)] for candidate in set(candidate_list)]
candidates_name = sorted(candidates_name, key=lambda x: x[1], reverse=True)

print("Election Results")
print("------------------")
print("Total Votes: ", str(total_votes))
print("------------------")

for candidate in candidates_name:
    percent_votes = (candidate[1] / total_votes) * 100
    print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})')
    
print("------------------")
print(f"Winner: {candidates_name[0][0]}")
print("------------------")



        
        
        
       

    

        