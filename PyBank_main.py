import os
import csv

pybank_csv = os.path.join("Resources", "budget_data.csv")

total_months = 0
PL_Total = 0

prior_month = 0
Monthly_chg = 0
Monthly_chg_total = 0
Monthly_chg_max = ["None",0]
Monthly_chg_min = ["None",0]


with open(pybank_csv) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")

	#skip header
	next(csv_reader)

	for row in csv_reader:
		total_months += 1
		PL_Total = PL_Total + int(row[1])
		

		if row[0] != "Jan-2010":		#first data row doesn't count
			Monthly_chg = int(row[1]) - prior_month
			Monthly_chg_total = Monthly_chg_total + Monthly_chg

			if Monthly_chg > Monthly_chg_max[1]:
				Monthly_chg_max[0] = row[0]
				Monthly_chg_max[1] = Monthly_chg


			if Monthly_chg < Monthly_chg_min[1]:
				Monthly_chg_min[0] = row[0]
				Monthly_chg_min[1] = Monthly_chg


		prior_month = int(row[1])		


Monthly_chg_avg = round(Monthly_chg_total/(total_months-1),2)

print('Financial Analysis')
print('-----------------------------')
print(f'Total Months: {total_months}')	
print(f'Total: ${PL_Total}')
print(f'Average Change: ${Monthly_chg_avg}')
print(f'Greatest Increase in Profits: {Monthly_chg_max[0]} (${Monthly_chg_max[1]})')
print(f'Greatest Decrease in Profits: {Monthly_chg_min[0]} (${Monthly_chg_min[1]})')


with open("pybank_output.txt","w",newline="") as datafile:
	writer = csv.writer(datafile)

	writer.writerow(["Financial Analysis"])
	writer.writerow(['-----------------------------'])
	writer.writerow([f'Total Months: {total_months}'])	
	writer.writerow([f'Total: ${PL_Total}'])
	writer.writerow([f'Average Change: ${Monthly_chg_avg}'])
	writer.writerow([f'Greatest Increase in Profits: {Monthly_chg_max[0]} (${Monthly_chg_max[1]})'])
	writer.writerow([f'Greatest Decrease in Profits: {Monthly_chg_min[0]} (${Monthly_chg_min[1]})'])