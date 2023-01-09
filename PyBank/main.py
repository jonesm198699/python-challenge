import os
import csv
budget_data = os.path.join("budget_data.csv")
with open('budget_data.csv', newline = "") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        csv_header = next(csvreader)
        revenue = []        
        month = []
        rev_change = []
        
        for row in csvreader:
            revenue.append(float(row[1]))
            month.append(row[0])

        print("Financial Analysis")
        print("------------------")
        print("Total Months:", len(month))
        print("Total Revenue: $", sum(revenue))

        for i in range(1, len(revenue)):
            rev_change.append(revenue[i] - revenue[i-1])
            avg_rev_change = sum(rev_change)/len(rev_change)
            max_rev_change = max(rev_change)
            min_rev_change = min(rev_change)

            max_rev_change_date = str(month[rev_change.index(max(rev_change))])
            min_rev_change_date = str(month[rev_change.index(min(rev_change))])

        print("Avereage Revenue Change: $", round(avg_rev_change))
        print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
        print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")


       
            