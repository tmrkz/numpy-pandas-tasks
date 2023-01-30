import pandas as pd

# 1. Загрузите базу данных из файла Titanic.csv.
df = pd.read_csv("Titanic.csv")
# print(df.head())

# 2. Загрузите базу данных так из файла еще раз, но так,
# чтобы столбец PassengerId был идентификатором,
# то есть номером строки (index).
df = pd.read_csv("Titanic.csv", index_col=0)
# print(df.head())

# 3.Удалите из базы строки с пропущенными значениями
# и сохраните изменения в самой базе.
# print(df.info())
df = df.dropna()
# print(df.info())

# 3. Выведите сводную информацию по базе данных:
# какие переменные в ней есть, какого они типа +
# сколько заполненных наблюдений в каждой столбце.
print(df.info())

# 4. Выведите сводную статистическую информацию
# по каждому количественному показателю в базе (описательные статистике).
print(df.describe())

# 5. Постройте гистограмму для переменной Возраст (Age),
# сделайте ее красного цвета, подпишите оси и добавьте заголовок графика.
import matplotlib.pyplot as plt

ax = df["Age"].plot.hist(color="red")
ax.set_title("Histogram")
ax.set_xlabel("Age")
ax.set_ylabel("Frequency")
plt.show()

# 6. Выведите описательные статистики для столбца Стоимость билета (Fare).
print(df["Fare"].describe())

# 7. Выведите названия столбцов в базе данных в виде списка (объект типа list).
print(list(df.columns))

# 8. Переименуйте столбец с классом пассажира из Pclass в Class.
new_cols = list(df.columns)
new_cols[1] = "Class"
df.columns = new_cols
# print(list(df.columns))

# 9. Выберите из базы данных все строки, которые
# соответствуют пассажирам женского пола, и сохраните их в новую базу female.
Female = pd.DataFrame(df[df["Sex"] == "female"])

# 10. Выберите из базы данных все строки, которые соответствуют
# выжившим пассажирам мужского пола младше 32 лет, и сохраните их в базу Ymale.
Ymale = df[(df["Survived"] == 1) & (df["Sex"] == "male") & (df["Age"] < 32)]

# 11. Выберите из базы данных все строки, которые соответствуют пассажирам 1 или 2 класса.
print(df[(df["Class"] == 1) | (df["Class"] == 2)])

# 12. Выберите из базы данных все строки, которые соответствуют выжившим пассажирам 1 или 2 класса.
print(df[((df["Class"] == 1) | (df["Class"] == 2)) & (df["Survived"] == 1)])


# 13. Добавьте в датафрейм столбец Female, состоящий из значений 0 и 1,
# где 1 соответствует пассажирам женского пола.
def isfem():
    res = []
    for now in df["Sex"]:
        if now == "female":
            res.append(1)
        else:
            res.append(0)
    return res


df["Female"] = isfem()
# print(df[["Sex", "Female"]])

# 1.Выведите на экран все уникальные значения в столбце Embarked.
print(df.Embarked.unique())

# 2. Сгруппируйте строки в датафрейме в соответствии со значениями переменной
# Survived и выведите средние значения всех количественных переменных по группам.
print(df.groupby("Survived").agg("mean"))

# 3. Сгруппируйте строки в датафрейме в соответствии со значениями
# переменной Sex и сохраните в отдельный датафрейм таблицу
# со средними и медианными значениями переменной Age
# по группам (мужчины и женщины).
a = df.groupby("Sex").agg(["mean", "median"]).loc["male"]
b = df.groupby("Sex").agg(["mean", "median"]).loc["female"]
print(a, b)

# 1. Приведите все названия столбцов в датафрейме к нижнему регистру и сохраните изменения.
old_cols = list(df.columns)
df.columns = [now.lower() for now in old_cols]

# 2. Выгрузите итоговый датафрейм в файл Titanic-new.csv.
df.to_csv("Titanic-new.csv")