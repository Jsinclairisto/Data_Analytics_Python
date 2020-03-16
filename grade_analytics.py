import csv, os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style 

# f = open('data.csv')
# csv_f = csv.reader(f)

data = [10, 44, 90, 30]
register = [0, 1, 2, 3]

df = pd.read_csv('data.csv', delimiter=',', index_col=0)

df['PercentGrade'].describe()

df['PercentGrade'].plot(kind="box")
df['PercentGrade'].plot(kind='hist', title='PercentGrade')

df.boxplot(column='PercentGrade', by='Test')
