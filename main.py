### INF601 - Advanced Programming in Python
### Cooper Weinhold
### Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt

accidents = pd.read_csv('Airplane_Crashes_and_Fatalities_Since_1908.csv', index_col=0)

print(accidents.head())