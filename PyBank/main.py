import csv
import os

# Define the file path
budget_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')
output_file = os.path.join('PyBank', 'analysis', 'financial_analysis.txt')

# Initialize variables to store required values
total_months = 0
net_total = 0
previous_profit_loss = 0
total_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Iterate through each row in the CSV
    for row in csvreader:
        # Count the number of months
        total_months = total_months + 1

        # Add the profit/loss to the net total
        net_total = net_total + int(row[1])

        # Calculate the change in profit/loss
        if total_months > 1:
            change = int(row[1]) - previous_profit_loss
            total_change += change
        

            # Check for greatest increase and decrease
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]

        # Update previous profit/loss for the next iteration
        previous_profit_loss = int(row[1])

# Calculate the average change
average_change = total_change / (total_months - 1)

# Print the analysis results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write results to a file
with open(output_file, "w", newline='') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
