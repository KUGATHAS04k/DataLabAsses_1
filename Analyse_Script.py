'''
author: Kugathas Ganeshan
date: 2026-02-20
description: This script is used to analyze the data from the CSV file and visualize it using matplotlib.
'''

#import necessary libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Load the data from the CSV file
data = pd.read_csv('/home/kugathas/Desktop/Python/Data_Lab_assignment1/data.csv')

#display the first few rows of the data
print(data.head())  

#display the summary statistics of the data
print(data.describe())


