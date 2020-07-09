import os
import pandas as pd

dirname = os.path.dirname(__file__)
path = os.path.join(dirname,'Resources','budget_data.csv')

data_df = pd.read_csv(path)
print(data_df.head())

total_pl = 0
total_months = len(data_df['Date'])
greatest_change = data_df['Profit/Losses'].max()
least_change = data_df['Profit/Losses'].min()
total_net_change = data_df['Profit/Losses'].sum()

for value in data_df['Profit/Losses']:
    total_pl += value

average_change = total_pl/total_months


output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net_change}\n"
    f"Average  Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_change} (${greatest_change})\n"
    f"Greatest Decrease in Profits: {least_change} (${least_change})\n")

print(output)

with open(dirname + '/output.txt', 'w') as file:
    file.write(output)