### INF601 - Advanced Programming in Python
### Cooper Weinhold
### Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = 'Airplane_Crashes_and_Fatalities_Since_1908.csv'
data = pd.read_csv(file_path)

# Convert 'Date' to datetime format and filter for crashes after 1970
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y', errors='coerce')
data_after_1970 = data[data['Date'].dt.year > 1970]

os.makedirs('charts', exist_ok=True)

# Function to filter and plot crashes by manufacturer
def plot_and_save_crashes_by_manufacturer(manufacturer_name, color, crashes=None):
    # Filter for manufacturer-related crashes
    manufacturer_crashes = data_after_1970[
        data_after_1970['Type'].str.contains(manufacturer_name, case=False, na=False)]

    # Extract the year of the crashes
    manufacturer_crashes['Year'] = manufacturer_crashes['Date'].dt.year

    # Count the number of crashes per year
    crashes_per_year = manufacturer_crashes.groupby('Year').size()

    # Plot the crashes per year
    plt.figure(figsize=(10, 6))
    crashes_per_year.plot(kind='bar', color=color)
    plt.title(f'Number of {manufacturer_name} Aircraft Crashes Per Year (After 1970)')
    plt.xlabel('Year')
    plt.ylabel('Number of Crashes')
    plt.grid(True)
    plt.xticks(rotation=45)
    #plt.show()

# Save the plot as a PNG file
    plt.savefig(f'charts/{crashes}')
    plt.close()  # Close the figure to free memory

# Plot and save for Boeing aircraft
plot_and_save_crashes_by_manufacturer('Boeing', 'skyblue', 'boeing_crashes.png')

# Plot and save for Lockheed aircraft
plot_and_save_crashes_by_manufacturer('Lockheed', 'lightcoral', 'lockheed_crashes.png')

# Plot and save for Cessna aircraft
plot_and_save_crashes_by_manufacturer('Cessna', 'lightgreen', 'cessna_crashes.png')

print("All charts have been saved in the 'charts' folder.")