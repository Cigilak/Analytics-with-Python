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

est = sm.OLS(Y_train, X2)
est2 = est.fit()
print(est2.summary())
#                            OLS Regression Results                            
#==============================================================================
#Dep. Variable:                  PRICE   R-squared:                       0.755
#Model:                            OLS   Adj. R-squared:                  0.745
#Method:                 Least Squares   F-statistic:                     77.10
#Date:                Thu, 12 Apr 2018   Prob (F-statistic):           6.06e-91
#Time:                        10:40:21   Log-Likelihood:                -984.91
#No. Observations:                 339   AIC:                             1998.
#Df Residuals:                     325   BIC:                             2051.
#Df Model:                          13                                         
#Covariance Type:            nonrobust                                         
==============================================================================
#                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
#const         32.8589      5.830      5.636      0.000      21.390      44.328
#CRIM          -0.1564      0.039     -4.022      0.000      -0.233      -0.080
#ZN             0.0385      0.016      2.371      0.018       0.007       0.071
#INDUS         -0.0251      0.071     -0.352      0.725      -0.165       0.115
#CHAS           0.7864      1.047      0.751      0.453      -1.273       2.846
#NOX          -12.9469      4.594     -2.818      0.005     -21.984      -3.909
#RM             4.0027      0.478      8.380      0.000       3.063       4.942
#AGE           -0.0116      0.015     -0.780      0.436      -0.041       0.018
#DIS           -1.3683      0.238     -5.750      0.000      -1.836      -0.900
#RAD            0.3418      0.084      4.072      0.000       0.177       0.507
#TAX           -0.0135      0.005     -2.877      0.004      -0.023      -0.004
#PTRATIO       -0.9889      0.152     -6.497      0.000      -1.288      -0.689
#B              0.0121      0.003      3.762      0.000       0.006       0.018
#LSTAT         -0.4726      0.060     -7.922      0.000      -0.590      -0.355
==============================================================================
#Omnibus:                      112.211   Durbin-Watson:                   1.999
#Prob(Omnibus):                  0.000   Jarque-Bera (JB):              468.704
#Skew:                           1.369   Prob(JB):                    1.67e-102
#Kurtosis:                       8.068   Cond. No.                     1.49e+04
==============================================================================

#Warnings:
#[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
#[2] The condition number is large, 1.49e+04. This might indicate that there are
#strong multicollinearity or other numerical problems.


# Linear regression with Sklearn
lin_reg = LinearRegression()
lin_reg.fit(X2, Y_train)
lin_reg.intercept_ , lin_reg.coef_
