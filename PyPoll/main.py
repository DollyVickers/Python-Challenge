import os
import csv

input_file='election_data.csv'

csv_input_path=os.path.join('election_data.csv')
txt_output_path=os.path.join('summary_doc','election_summary.txt')

candidates,total_candidates,candidate_perc,candidate_total,summaries=([] for i in range(5))

with open(csv_input_path, mode='r', newline='') as poll_data:
    reader=csv.reader(poll_data,delimiter=',')

    next(reader)

    num_rows=0

    for row in reader:
        total_candidates.append(row[2])
        num_rows += 1

sorted_candidates=sorted(total_candidates)

for i in range(num_rows):
    if sorted_candidates[i - 1]!=sorted_candidates[i]:
        candidates.append(sorted_candidates[i])

print("\nElection Results")
print("_" =40)
print("Total Voters:",num_rows)
print("_"=40)

for j in range

