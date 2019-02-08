import os
import csv

csvpath=os.path.join('Resources','budget_data.txt')

with open(csvpath, newline='') as csvfile:

        csvreader=csv.reader(csvfile, delimiter=',')

        print(csvreader)

        csv_header=next(csvreader)
        print(f"CSV header: {csv_header}")

        for row in csvreader:
                print(row)
import os
import csv

root_path=os.path.join(os.getcwd(),".")
data_path=os.path.join(root_path,"raw_data")
output_path=os.path.join(root_path,"output")

filepaths=[]
for file in os.listdir(data_path):
        if file.endwith(".csv"):
                filepaths.append(os.path.join(data_path,file))

for file in filepaths:
        tot_revenue=0
        month_count=0
        revenue=0
        data_dict_list=[]
        with open(file,newline="") as csvfile:
                csvreader=csv.DictReader(csvfile)
                for row in csvreader:

                        rev_diff={"rev_diff": int("{Revenue}".format(**row)) - revenue}
                        rev_change=rev_change + int("{Revenue}".format(**row)) - revenue
                        revenue=int("{Revenue}".format(**row))
                        tot_revenue += revenue
                        month_count += 1
                        data_dict_list.append({**row,**rev_diff}) 

increase_dict=dict(max(data_dict_list, key=lambda x:x["rev_diff"]))
decrease_dict=dict(min(data_dict_list, key=lambda x:x["rev_diff"]))

increase_date= increase_dict.get("Date")
increase_revdiff= increase_dict.get("rev_diff")
decrease_date= decrease_dict.get("Date")
decrease_revdiff= decrease_dict.get("rev_diff")

first_row= data_dict_list[0]
first_row_revdiff=first_row.get("rev_diff")
rev_change= rev_change - first_row_revdiff
avg_change= int(rev_change/(month_count - 1))

_, filename= os.path.split(file)
filename, _=filename.split(".csv")

print(
        f"Financial Analysis - {filename}\n"
        f"-------------------------------\n"
        f"Total Months: {month_count}\n"
        f"Total Revenue: ${tot_revenue}\n"
        f"Average Revenue Change: ${avg_change}\n"
        f"Greatest Increase in Revenue: {increase_date} (${increase_revdiff})\n"
        f"Greatest Decrease in Revenue: {decrease_date} (${decrease_revdiff})\n"
)

text_path=os.path.join(output_path, filename + ".txt")
with open(text_path, "w") as text_file:
        text_file.write(
        f"Financial Analysis: {filename}\n"
        f"------------------------------\n"
        f"Total Months: {month_count}\n"
        f"Total Revenue: ${tot_revenue}\n"
        f"Average Revenue Change: ${avg_change}\n"
        f"Greatest Increase in Revenue: {increase_date} (${increase_revdiff})\n"
        f"Greatest Decrease in Revenue: {decrease_date} (${decrease_revdiff})\newline"
        ) 