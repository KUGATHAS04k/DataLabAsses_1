'''
Author: Kugathas Ganeshan
Date: 2026-02-20
Description: This script analyzes electricity access data from a CSV file and creates visualizations using matplotlib.
'''

# Import necessary libraries:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file:
data = pd.read_csv('/home/kugathas/Desktop/Python/Data_Lab_assignment1/data.csv')

# Display the first few rows of the data:
print(data.head())  

# Display the summary statistics of the data:
print(data.describe())

# Create dataframe for the analysis:
df = pd.DataFrame(data)

# Display the information about the dataframe:
df.info()
print(df.info())

# Add a new column for no of countries in the data:
df.insert(1, 'No of Countries', range(1, len(df) + 1))

# Display the updated dataframe:
print(df.head())

'''
Visualize the data using matplotlib.

1.Task: Create a line plot to single country.
2.Task: Create a line plot to multiple countries.
3.Task: Create a pie chart to show the distribution of electricity access in 2020 for all countries.

'''
# Task 1: Create a line plot to single country.(e.g. Sri Lanka):

country_name = 'Sri Lanka' ##you can change the country
selected_country = df[df['Country Name'] == country_name]

# Select the years for the x axis and the corresponding values for the y axis:
years = [str(year) for year in range(2000, 2021)]##year need to converted into string because the column names are in string format
sin_values = selected_country[years].values.flatten()

# Building the line chart:
plt.figure(figsize=(6, 4))
plt.plot(years, sin_values, marker='o', linestyle='-', color='b')
plt.title(f'Electricity Access in {country_name} (2000-2020)')
plt.xlabel('Year')
plt.ylabel('Electricity Access (%)')
plt.grid(True)
plt.xticks(rotation= 45) ##rotate the x-axis labels
plt.legend([country_name])
plt.tight_layout() ##adjust the layout to prevent overlap
plt.show()

# Bulding the bar chart for single country:
plt.figure(figsize=(6,4))
plt.bar(years, sin_values) 
plt.xlabel('Year')
plt.ylabel('Electricity Access (%)')
plt.xticks(rotation= 45)
plt.legend([country_name])
plt.show()

# Task 2: Create a line plot to multiple countries.(e.g. Sri Lanka, India, Bangladesh):


plt.figure(figsize=(12, 6))

for select_multi_country in ['India', 'Zimbabwe', 'Bangladesh', 'Sri Lanka']: ##you can change the country
    multi_values = df[df['Country Name'] == select_multi_country][years].values.flatten()
    plt.plot(years, multi_values, label=select_multi_country)
plt.xlabel('Year')
plt.ylabel('Electricity Access (%)')
plt.grid(True)
plt.xticks(rotation=45) ##rotate the x-axis labels    
plt.legend()
plt.show()

# Task 3: Create a pie chart to show the distribution of electricity access in 2020 for all countries:

# Select the data for the year 2020:
data_2020 = df['2020'].dropna() ##drop the missing values

slices = [
    data_2020[data_2020 == 100].count(), ##count the 100% access
    data_2020[(data_2020 >= 90) & (data_2020 < 100)].count(), ##90 - 99% access
    data_2020[(data_2020 >= 50) & (data_2020 < 90)].count(), ##50 - 89% access
    data_2020[data_2020 < 50].count() ##less than 50% access
] 

labels = ['100% Access', 'High (90-99%)', 'Medium (50-89%)', 'Low (<50%)']
colors = ['#003f5c', '#7a5195', '#ef5675', '#ffa600']

# Create the pie chart:
plt.figure()
plt.pie(
    slices,
    labels= labels,
    colors= colors,
    autopct= '%1.1f%%', ##shows the percentage on the slice
    startangle= 140, ##rotates the start of the chart
    explode= (0.1, 0, 0, 0), ##pulls the '100% Access' slice out 
    shadow = True ##add 3d look
)

# Add the title:
plt.title('Global Electricity Access Distribution (2020)')
plt.axis('equal') ##this feature make the pie chart circle, not an oval shape
plt.show()

'''
This is End here

'''