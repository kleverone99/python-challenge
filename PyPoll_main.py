import os
import csv

pypoll_csv = os.path.join("Resources", "election_data.csv")

votes_total = 0
votes = {"Candidate":[],"Votes":[]}
counter = 0

with open(pypoll_csv) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")

	#skip header
	next(csv_reader)

	for row in csv_reader:
		votes_total += 1

		if row[2] not in votes["Candidate"]:
			votes["Candidate"].append(row[2])
			votes["Votes"].append(0)

		if row[2] in votes["Candidate"]	:
			index = votes["Candidate"].index(row[2])
			votes["Votes"][index] += 1

for row in range(len(votes["Votes"])): 
	#print (votes["Votes"][row])
	if votes["Votes"][row] > counter:
		counter = votes["Votes"][row]
		winner = votes["Candidate"][row]

	
print ('Election Results')
print ('---------------------')
print (f'Total Votes: {votes_total}')
print ('---------------------')

for row in range(len(votes["Candidate"])): 
	print(f'{votes["Candidate"][row]}: {round(votes["Votes"][row]/votes_total*100, 2)}% ({votes["Votes"][row]})')

print ('---------------------')
print (f'Winner: {winner}')
print ('---------------------')

with open("pypoll_output.txt","w",newline="") as datafile:
	writer = csv.writer(datafile)

	writer.writerow(['Election Results'])
	writer.writerow(['-------------------------'])
	writer.writerow([f'Total Votes: {votes_total}'])
	writer.writerow(['-------------------------'])
	for row in range(len(votes["Candidate"])): 
		writer.writerow([f'{votes["Candidate"][row]}: {round(votes["Votes"][row]/votes_total*100, 2)}% ({votes["Votes"][row]})'])
	writer.writerow(['-------------------------'])
	writer.writerow([f'Winner: {winner}'])
