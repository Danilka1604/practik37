import pandas as pd
import numpy as np

df = pd.read_csv('train_2.csv')

relatives_array = df[['SibSp', 'Parch']].values

total_relatives = np.sum(relatives_array)

print("Общее количество родственников на борту:", total_relatives)

passenger_with_most_relatives = np.argmax(np.sum(relatives_array, axis=1))

print("Пассажир с наибольшим количеством родственников:")
print(df.iloc[passenger_with_most_relatives])
