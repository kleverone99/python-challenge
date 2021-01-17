import os
import csv

#Read csv
pypoll_csv = os.path.join("Resources", "election_data.csv")

#starting values in variables
votes_total = 0
votes = {"Candidate":[],"Votes":[]}
counter = 0

with open(pypoll_csv) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")

	#skip header
	next(csv_reader)

	for row in csv_reader:
		#counting total votes
		votes_total += 1

		#adding new candidates to the list
		if row[2] not in votes["Candidate"]:
			votes["Candidate"].append(row[2])
			votes["Votes"].append(0)

		#counting candidate votes
		if row[2] in votes["Candidate"]	:
			index = votes["Candidate"].index(row[2])
			votes["Votes"][index] += 1

#Finding winner
for row in range(len(votes["Votes"])): 
	if votes["Votes"][row] > counter:
		counter = votes["Votes"][row]
		winner = votes["Candidate"][row]

#print to terminal	
print ('Election Results')
print ('---------------------')
print (f'Total Votes: {votes_total}')
print ('---------------------')

for row in range(len(votes["Candidate"])): 
	print(f'{votes["Candidate"][row]}: {round(votes["Votes"][row]/votes_total*100, 2)}% ({votes["Votes"][row]})')

print ('---------------------')
print (f'Winner: {winner}')
print ('---------------------')

#create txt file of results
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
