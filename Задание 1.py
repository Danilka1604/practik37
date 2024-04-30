import pandas as pd
import numpy as np

df = pd.read_csv('train_2.csv')
survived_array = df['Survived'].values
total_survived = np.sum(survived_array)
print("Общее количество выживших пассажиров:", total_survived)
