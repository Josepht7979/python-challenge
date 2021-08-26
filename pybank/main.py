import os
import csv

pyBank = os.path.join("Resources","budget_data.csv")

with open (pyBank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_headers = next(csvreader, None)

    months = []
    profit = []

    for row in csvreader:
        months.append(row[1])
        profit.append(int(row[1]))

    total_months = len(months)
    print (f"Total Months: {total_months}")

#------------------------------------------
    
    net_total = 0
    i = 1
    for i in range(total_months):
        net_total = net_total + int(profit[i])
    print (f"Total: ${net_total}")

#------------------------------------------
# Average change per month
# change in profit/loss column per month
    change = []
    j = 0
    k = 0

    for j in range (1, total_months):
        if j == 0:
            change.append(0)
        else:
            change.append(int(profit[j])-int(profit[k]))
            k += 1
#---------------------------------------------------------
# Add monthly changes and divide by total_months
    average_monthly_change = ((sum(change))/(len(change)))
    print (f"Average Change: ${round((average_monthly_change),2)}")

#---------------------------------------------------------   
# greatest increase in profits
    max_change = max(change)
    print (f"Greatest Increase in Profits: ${max_change}")
# greatest decrease in profits
    min_change = min(change)
    print (f"Greatest Decrease in Profits:  ${min_change}")


# Print to text file
with open('Results.txt', "w") as text:
        text.write(f"Total Months: {total_months}\n")
        text.write(f"Total: ${net_total}\n")
        text.write(f"Average Change: ${round((average_monthly_change))}\n")
        text.write(f"Greatest Increase in Profits: ${max_change}\n")
        text.write(f"Greatest Decrease in Profits:  ${min_change}\n")

