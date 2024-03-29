import csv 


# Set_input_/ output_files ----check_Readme_reference---------------------------------------
csv_file = "Resources/budget_data.csv"
   

output_text_file_path = "analysis/budget_outcome.txt"

# set_varibales_for_questions-----------check_Readme_reference---------------------------------------------
total_number_of_months = 0
net_total = 0
previous_profit_loss = 0
profit_losses_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# csv_reading_and_scan_rows -----------class_notes------------------------------
with open(csv_file) as cf:
    csvscanner = csv.reader(cf, delimiter=",")
    next(csvscanner)  
    for row in csvscanner:
        # Find_total_months--------class_notes----------
        total_number_of_months += 1
        net_total += int(row[1])
        
        # Find change_in_profit_loss-------------------class_notes------------------------
        profit_loss_change = int(row[1]) - previous_profit_loss
        profit_losses_changes.append(profit_loss_change)
        previous_profit_loss = int(row[1])
        
        # Find_greatest_increase-and_decrease_--------check_Readme_reference------------------------------------
        if profit_loss_change > greatest_increase[1]:
            greatest_increase = [row[0], profit_loss_change]
        if profit_loss_change < greatest_decrease[1]:
            greatest_decrease = [row[0], profit_loss_change]

# Find_avg_change----------check_Readme_reference------------------------------------------------------------
avg_change = round(sum(profit_losses_changes[1:]) / (total_number_of_months - 1), 2)

# Format_Budget_Outcome_results--------check_Readme_reference------------------------------------------------------------
budget_outcome = f"""
----------------------------
Financial Analysis
-----------------------------
Total Months: {total_number_of_months}
Total: ${net_total}
Average Change: ${avg_change}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})

-------------------------------
"""

# Print analysis in terminal---------class_notes----------------------------------------------
print(budget_outcome)

# Export_Budget_Outcome_text_file--------class_notes-------------------------------------------------
with open(output_text_file_path, "w") as PyBank_txtfile:
    PyBank_txtfile.write(budget_outcome)

print("Congratulations, it's Complete... check file budget_outcome.txt")
