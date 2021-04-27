import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

poke_data = pd.read_csv("pokemon_data.csv")
# print(poke_data)

linear_col = poke_data.iloc[:,4:10]
# print(linear_col)

hp = poke_data[["HP"]]
speed = poke_data[["Speed"]]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(speed,hp,test_size=0.33,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)
Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(x_train, y_train)
tahmin = lr.predict(x_test)

x_train = x_train.sort_index()
y_train = y_train.sort_index()

plt.plot(x_train, y_train)
plt.plot(x_test, lr.predict(x_test))

plt.title("HPye göre Speed")
plt.xlabel("Speed")
plt.ylabel("HP")



