
import csv

# Set_input_/ output_files-----------check_Readme_reference---------------------------------------------
csv_file = "Resources/election_data.csv"

output_text_file_path = "analysis/voting_outcome.txt"

# set_varibales_for_questions----------check_Readme_reference---------------------------------------------------------
total_votes_casted = 0
candidates_pos = {}
candidate_winner = ""
votes_4_winner = 0

# csv_reading_and_scan_rows---------class_notes----------------------------------------------
with open(csv_file) as cf:
    csvscan = csv.reader(cf, delimiter=",")
    next(csvscan)  
    for row in csvscan:
        # total votes------class_notes---------------------------
        total_votes_casted += 1
        
        # votes per candidate-----------class notes-----------------------------
        candidate_name = row[2]
        if candidate_name in candidates_pos:
            candidates_pos[candidate_name] += 1
        else:
            candidates_pos[candidate_name] = 1

# Find percentage of votes per candidate & find the winner--------------check_Readme_reference-------------------------
results = ""
for candidate, votes in candidates_pos.items():
    percentage = (votes / total_votes_casted) * 100
    results += f"{candidate}: {percentage:.3f}% ({votes})\n"
    if votes > votes_4_winner:
        candidate_winner = candidate
        votes_4_winner = votes

# Format_voting_outcome_results----------check_Readme_reference------------------------------------------------------
voting_outcome = f"""
Election Results
-------------------------
Total Votes: {total_votes_casted}
-------------------------
{results}
-------------------------
Winner: {candidate_winner}
-------------------------
"""

# Print analysis in terminal----------class_notes-----------------------------
print(voting_outcome)

# Export analysis results to a text file--------class_notes--------------------------------------------
with open(output_text_file_path, "w") as PyPoll_txtfile:
    PyPoll_txtfile.write(voting_outcome)

print("Congratulations, it's Complete... check file voting_outcome.txt")
