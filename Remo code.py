
# Function to calculate monthly cost
def calculate_monthly_cost(row, start_index=4, end_index=9):
    try:
        values = [float(str(value).replace(",", "").replace("$", "")) for value in row[start_index:end_index]]
        return sum(values)
    except ValueError:
        return 0  # Handle non-numeric values gracefully

# Create new columns for primary and secondary monthly costs
df["Primary_Monthly_Cost"] = 0
df["Secondary_Monthly_Cost"] = 0

# Identify process and calculate monthly costs using apply and lambda function
df["Primary_Monthly_Cost"] = df.apply(lambda row: calculate_monthly_cost(row) if row["Process"] == "Primary" else 0, axis=1)
df["Secondary_Monthly_Cost"] = df.apply(lambda row: calculate_monthly_cost(row) if row["Process"] == "Secondary" else 0, axis=1)

# Display the DataFrame with new columns
print(df)
