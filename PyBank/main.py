import os
import csv
#Path to the file

budget_csv = os.path.join ('Resources', 'budget_data.csv')
#Read the header row
with open(budget_csv, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    next(reader)

 # Initialize variables

    count = 0 
    total = 0
    prev_revenue = 0 
    revenue_change_list = []
    month_of_change = []
    total_change = 0 
    
    for row in reader:
        count = count + 1
        current_revenue = int(row[1])
        total = total + current_revenue
        
        if prev_revenue != 0 :
            revenue_change = current_revenue - prev_revenue
            revenue_change_list.append(revenue_change)
            month_of_change.append(row[0])
            total_change = total_change + revenue_change
            
        prev_revenue = current_revenue

 #Calculate average change
    
    avg_change = total_change / (count - 1)

   ## Print the results 
    print(f'Total number of months: {count}')
    print(f'Total profit/loss: ${total}')
    print(f'Total change: {total_change}')
    print(f'Average change: ${avg_change:.2f}')

 # Update net total amount of "Profit/Losses"
    
    max_increase = max(revenue_change_list)
    max_increase_month = month_of_change[revenue_change_list.index(max_increase)]
  
    print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
  
    max_decrease = min(revenue_change_list)
    max_decrease_month = month_of_change[revenue_change_list.index(max_decrease)]

    print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})")

 #The PyBank project simplifies and accelerates financial data analysis, offering clear and concise reports that highlight essential financial metrics and trends.


output = (
    
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {count}\n"
    f"Total: ${total}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n"
    f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n")

print(output)

output_file = "./analysis/result.txt"
with open(output_file, "w") as f:
    f.write(output)
