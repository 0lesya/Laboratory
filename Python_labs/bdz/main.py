import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
pd.options.mode.chained_assignment = None

train_dataset = pd.read_csv('train.csv')
print(train_dataset.head())

'''Задание №1
С помощью модуля pandas выведите статистику погибших/выживших отдельно
для мужчин и женщин в каждом классе (Pclass).
'''
print('\n\tСтатистика выживших по гендеру.')
print(train_dataset.groupby(['Sex', 'Pclass', 'Survived'])['PassengerId'].count())

'''Задание №2
С помощью модуля pandas выведите статистику по всем числовым полям,
отдельно для мужчин и женщин.'''
print('\n\tСтатистика по числовым полям.')
numbersColon = train_dataset.select_dtypes(include='number')
print(train_dataset.groupby(['Sex'])[numbersColon.columns].count())

'''Задание №3
Определите, влияет ли порт посадки на выживаемость.'''
print('\n\tВлияние порта посадки на выживаемость')
print(train_dataset.groupby(['Embarked', 'Survived'])['PassengerId'].count())

'''Задание №4
4.1. Выведите топ 10 популярных имён.'''
print('\n\tТоп 10 популярных имен')
print(train_dataset["Name"].apply(lambda full_name: full_name.split(',')[1].split()[1]).value_counts()[:10])

'''4.2. Выведите топ 10 популярных фамилий.'''
print('\n\tТоп 10 популярных фамилий')
print(train_dataset["Name"].apply(lambda full_name: full_name.split(',')[0]).value_counts()[:10])

'''Задание №5
Заполните все отсутствующие в train.csv значения медианой (по столбцу).'''
print('\n\tЗаполнение отсутствующих значений.')
for name in train_dataset.columns.tolist():
    if train_dataset[name].isnull().sum() != 0:
        try:
            train_dataset[name] = train_dataset[name].fillna(train_dataset[name].median())
        except Exception as e:
            train_dataset[name].value_counts().idxmax()
        finally:
            print('Дополненный столбец: ', name)


'''Задание №6
На основе статистики попытайтесь предсказать выживаемость для пассажиров из файла test.csv. '''
print('\n\tОбучение моделей.')
# для начала выберем столбцы, которые наиболее явным образом влияют на выживаемость:
# это гендер, класс, возраст, тариф

columns_target = ['Survived']
columns_train = ['Pclass', 'Sex', 'Age', 'Fare']

# разделим обучающий датасет на входные и целевые значения
X = train_dataset[columns_train]
Y = train_dataset[columns_target]

# преобразуем строковые значения Sex в int
dict_sex = {'male': 0, 'female': 1}
X['Sex'] = X['Sex'].apply(lambda x: dict_sex[x])

# обучим две разные модели, чтобы оценить качество обучения
model1 = RandomForestClassifier()
model1.fit(X, np.ravel(Y))

model2 = svm.LinearSVC(dual=False)
model2.fit(X, np.ravel(Y))

# обработаем тестовый датасет
test_dataset = pd.read_csv('test.csv')
X_pred = test_dataset[columns_train]
X_pred['Sex'] = X_pred['Sex'].apply(lambda x: dict_sex[x])
X_pred['Age'] = X_pred['Age'].fillna(X_pred['Age'].median())
X_pred['Fare'] = X_pred['Fare'].fillna(X_pred['Fare'].median())
print('Предсказание выживаемости по модели RandomForestClassifier: ')
Y_pred = model1.predict(X_pred)
print(Y_pred)
print('Предсказание выживаемости по модели LinearSVC: ')
Y_pred = model2.predict(X_pred)
print(Y_pred)

# чтобы сравнить модели, насильно разделим обучающий датасет на обучающую и тестовую выборки
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
# обучим две разные модели, чтобы оценить качество обучения
model1 = RandomForestClassifier()
model1.fit(X_train,  np.ravel(Y_train))

model2 = svm.LinearSVC(dual=False)
model2.fit(X_train,  np.ravel(Y_train))
print('Предсказание выживаемости по модели RandomForestClassifier: ')
model1.predict(X_test)
print(model1.score(X_test, Y_test))
print('Предсказание выживаемости по модели LinearSVC: ')
model2.predict(X_test)
print(model2.score(X_test, Y_test))

'''Задание №8
С помощью библиотеки matplotlib отобразите гистограмму зависимости возраста (в годах) от выживаемости.'''
dict_surv = train_dataset.groupby(['Age'])['Survived'].sum()
plt.title('Гистограмма зависимости выживаемости от возраста.')
plt.xlabel('Age')
plt.ylabel('Survived')
plt.bar(x=dict_surv.index,  height=dict_surv.values)
plt.show()
