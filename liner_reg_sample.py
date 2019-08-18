import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt

#収集したデータと仮定
x_data = np.arange(-3, 10, 0.1).reshape(-1, 1)
y_data = (1/2) * x_data + np.random.normal(0.0, 0.5, len(x_data)).reshape(-1, 1)

#学習用データとする
x_train = x_data[70:]   #70から最後まで
y_train = y_data[70:]

#モデルを学習データにフィットさせる
reg = linear_model.LinearRegression()
reg.fit(x_train, y_train)

#テストデータ
x_test = x_data[:71]    #最初から70まで（インデックス+1の値で指定）
y_test = y_data[:71]

#予測
pred = reg.predict(x_test)

#決定係数
print('score:', reg.score(x_test, y_test))

#相関係数
print('corr:', np.corrcoef(y_test.reshape(1, -1), pred.reshape(1, -1))[0, 1])

#RMSE
print('RMSE:', sqrt(mean_squared_error(y_test, pred)))

plt.scatter(x_test, y_test, color='blue')
plt.plot(x_test, pred, color='red')
plt.show()