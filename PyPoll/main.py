#Necessary Import
import csv

#Define files to be used in the program
poll_csv = "Resources/election_data.csv"
result_file = "Analysis/election_analysis.txt"

#Define Variables
vote_count=0
candidate_dict={}
output_str=""
output_line="-------------------------\n"

#Open the file
with open(poll_csv, newline='') as poll_file:
    poll_reader=csv.reader(poll_file, delimiter=",")
    
    #Skip the header
    header=next(poll_reader)

    #Loop to count the vote and build candidate dictionary along with respective count
    for row in poll_reader:
        vote_count=vote_count+1			#Count the vote

		#check if current candidate already exists in the candidate dictionary, and 
		# increment the respective vote counter (which is stored as "Value" in the dictionary)
        if row[2] in candidate_dict.keys() :
            candidate_dict[row[2]]= candidate_dict[row[2]] +1   
        else:
            candidate_dict[row[2]]=1	

    #Building output string        
    output_str=(f"\nElection Results\n"
                f"{output_line}"
                f"Total Votes: {vote_count}\n"
                f"{output_line}"
               )

    #adding candidate details to the output string
    for i in candidate_dict:
        output_str=output_str+f"{i}: {(candidate_dict[i]/vote_count)*100:.3f}% ({candidate_dict[i]})\n"

    #finding max/min votes, Winning candidate and adding to output string
    candidate_vote_count=list(candidate_dict.values())
    candidate_names=list(candidate_dict.keys())
    output_str = (f"{output_str}"
                  f"{output_line}"
                  f"Winner: {candidate_names[candidate_vote_count.index(max(candidate_vote_count))]}\n"
                  #f"Winner: {k[v.index(max(v))]}  with {max(v)} votes\n"
                  f"{output_line}"
                 )

#Output to console
print(output_str)    
    
#Write result to disk        
with open(result_file, "w") as out_file:
    out_file.write(output_str) #Write result to disk      