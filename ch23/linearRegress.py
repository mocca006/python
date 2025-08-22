from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

housing = fetch_california_housing()
x_train, x_test, y_train, y_test = train_test_split(housing.data, housing.target, test_size=0.2, random_state=1)
std_x = StandardScaler()
x_train = std_x.fit_transform(x_train)
x_test = std_x.transform(x_test)
std_y = StandardScaler()
y_train = std_y.fit_transform(y_train.reshape(-1, 1))
y_test = std_y.transform(y_test.reshape(-1, 1))
lr = LinearRegression()
lr.fit(x_train, y_train)
print('權重值：{}'.format(lr.coef_)) 
print('偏置值：{}\n'.format(lr.intercept_))

y_predict = std_y.inverse_transform(lr.predict(x_test))
y_real = std_y.inverse_transform(y_test)
for i in range(5):
    print('預測值{}：{}，真實值：{}'.format(i+1, y_predict[i], y_real[i]))
merror = mean_squared_error(y_real, y_predict)
print('平均方差：{}'.format(merror))
