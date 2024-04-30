import pandas as pd
import numpy as np

df = pd.read_csv("train_2.csv")

age_fare_array = df[['Age', 'Fare']].values
age_fare_array = age_fare_array[~np.isnan(age_fare_array[:, 0])]
sorted_age_fare_array = age_fare_array[np.argsort(age_fare_array[:, 0])]

youngest_passenger = sorted_age_fare_array[0]
oldest_passenger = sorted_age_fare_array[-1]

print(f"Информация о самом молодом пассажире (возраст, стоимость билета): {youngest_passenger}")
print(f"Информация о самом старом пассажире (возраст, стоимость билета): {oldest_passenger}")