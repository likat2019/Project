#место для твоего кода
import pandas as pd 
import matplotlib.pyplot as plt 
 
df = pd.read_csv('menu.csv') 
 
print('В завтраках каллорий больше чем в десертах:') 
 
calories_breakfast = df.groupby(by = 'Category')['Calories'].mean() 
print('Калорий в завтраках', round(calories_breakfast['Breakfast'], 2)) 
calories_dessert = df.groupby(by = 'Category')['Calories'].mean() 
print('Калорий в десертах', round(calories_dessert['Desserts'], 2)) 
 
Scalories = pd.Series(data=[calories_breakfast['Breakfast'], calories_dessert['Desserts']], 
    index=['калории в завтраках', 'калории в десертах']) 
Scalories.plot(kind='pie', y='Calories') 
plt.show() 
 
print('Максимальная порция свинины и говядины, равна максимальной порции курицы и рыбы') 
 
serving_size_pork = df.groupby(by = 'Category')['Serving Size'].max() 
print('максимальная порция говядины и свинины:', serving_size_pork['Beef & Pork']) 
serving_size_chicken = df.groupby(by = 'Category')['Serving Size'].max() 
print('максимальная порция курицы и рыбы:', serving_size_chicken['Chicken & Fish']) 
 
food = pd.Series(data=[280, 280], 
    index=['максимальная порция говядины и свинины', 'максимальная порция курицы и рыбы']) 
food.plot(kind='bar') 
plt.show() 


sugar = round(df.groupby(by = 'Category')['Sugars'].mean())
print('сахара в десерте больше чем в напитках')
print('Среднее число сахара в десерте', sugar['Desserts'])
print('Среднее число сахара в напитках', sugar['Beverages'])
sugar.plot(kind = 'barh')
plt.xlabel('Sugars')
plt.show()