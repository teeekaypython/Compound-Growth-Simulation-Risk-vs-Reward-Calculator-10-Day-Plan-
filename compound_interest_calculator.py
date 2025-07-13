import csv

# Parameters
starting_balance = 5  # Initial balance in dollars
risk_percentage = 10 / 100  # 10% risk per trade
percentage_2_5 = 2.5 / 100  # 2.5% for calculation
payout_percentage = 400 / 100  # 92% payout
days = 10  # Number of days

# Initialize results
detailed_results = []

# Reset starting balance
daily_balances = [starting_balance]

# Calculate daily values
for day in range(1, days + 1):
    current_balance = daily_balances[-1]
    bet_amount = current_balance * risk_percentage  # 10% risk
    profit = bet_amount * payout_percentage  # 92% payout
    new_balance = current_balance + profit

    # 2.5% dollar value
    two_point_five_percent_value = current_balance * percentage_2_5

    # Save daily details
    detailed_results.append((
        day,
        round(current_balance, 2),
        round(bet_amount, 2),
        round(profit, 2),
        round(two_point_five_percent_value, 2)
    ))

    # Update balance for the next day
    daily_balances.append(new_balance)

# Write results to a CSV file
output_file = f"compound interest.csv"

with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["Day", "Balance ($)", "10% Bet Amount ($)", "Profit from Bet ($)", "2.5% Dollar Value ($)"])

    # Write the daily results
    writer.writerows(detailed_results)

print(f"Results saved to {output_file}")
