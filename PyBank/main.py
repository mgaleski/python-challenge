import csv
import os

file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

total_months = 0
month_of_change = []
monthly_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0


with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)

    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])


        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        monthly_changes = monthly_changes + [net_change]
        month_of_change = month_of_change + [row[0]]


        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change


        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change


net_monthly_avg = sum(monthly_changes) / len(monthly_changes)

analysis = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(analysis)

with open(file_to_output, "w") as txt_file:
    txt_file.write(analysis)