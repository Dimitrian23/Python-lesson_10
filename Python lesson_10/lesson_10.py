import pandas as pd
import random

# Создаем DataFrame
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получаем уникальные значения из столбца
unique_values = data['whoAmI'].unique()

# Создаем новый DataFrame, в котором каждое уникальное значение станет отдельным столбцом
one_hot_data = pd.DataFrame()
for value in unique_values:
    one_hot_data[value] = (data['whoAmI'] == value).astype(int)

# Выводим результат
print(one_hot_data.head())