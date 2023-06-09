import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

# создание нового DataFrame, содержащего столбцы one hot
one_hot_data = pd.DataFrame()

# получение уникальных категорий в исходном столбце
categories = data['whoAmI'].unique()

# создание бинарных столбцов для каждой категории и заполнение их нулями
for category in categories:
    one_hot_data[category] = 0

# заполнение бинарных столбцов соответствующими значениями
for i, row in data.iterrows():
    category = row['whoAmI']
    one_hot_data.loc[i, category] = 1

one_hot_data.head()