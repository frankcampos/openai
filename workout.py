import pandas as pd

# Create a date range for the year 2023
start_date = '1/1/2023'
end_date = '12/31/2023'
dates = pd.date_range(start_date, end_date)

# Create a dataframe with the date range as the index
df = pd.DataFrame(index=dates)

# Add columns for exercise, sets, reps, and weight
df['Exercise'] = ""
df['Sets'] = ""
df['Reps'] = ""
df['Weight'] = ""

# Save the dataframe to an Excel file
df.to_excel("workout_tracker_2024.xlsx")
print("Excel sheet created!")
