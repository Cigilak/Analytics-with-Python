from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import pandas as pd
import sklearn
import sklearn.cross_validation
import statsmodels.api as sm

boston = load_boston()
print(boston.data.shape)
print(boston.DESCR)
bos = pd.DataFrame(boston.data)
bos.head(2)

bos.columns = boston.feature_names
bos.describe()
bos['PRICE'] = boston.target
Y = bos['PRICE']
Y.head(2)
X = bos
X = bos.drop('PRICE', axis = 1)

X_train, X_test, Y_train, Y_test = sklearn.cross_validation.train_test_split(X, Y, test_size = 0.33, random_state = 5)
X2 = sm.add_constant(X_train)
est = sm.OLS(Y, X2)
est = sm.OLS(Y_train, X2)
est2 = est.fit()
print(est2.summary())
