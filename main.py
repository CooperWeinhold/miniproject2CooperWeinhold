### INF601 - Advanced Programming in Python
### Cooper Weinhold
### Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Airplane_Crashes_and_Fatalities_Since_1908.csv'
data = pd.read_csv(file_path)

# Convert 'Date' to datetime format and filter for crashes after 1970
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y', errors='coerce')
data_after_1970 = data[data['Date'].dt.year > 1970]

# Filter for Boeing-related crashes
boeing_crashes = data_after_1970[data_after_1970['Type'].str.contains('Boeing', case=False, na=False)]

# Extract the year of the crashes
boeing_crashes['Year'] = boeing_crashes['Date'].dt.year

# Count the number of crashes per year
crashes_per_year = boeing_crashes.groupby('Year').size()

# Plot the crashes per year
plt.figure(figsize=(10, 6))
crashes_per_year.plot(kind='bar', color='skyblue')
plt.title('Number of Boeing Aircraft Crashes Per Year (After 1970)')
plt.xlabel('Year')
plt.ylabel('Number of Crashes')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()