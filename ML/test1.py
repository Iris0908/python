import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

df = pd.read_csv("C:/work/git/python/ML/FuelConsumptionCo2.csv", engine="python")

# take a look at the dataset
df.head()

# summarize the data
df.describe()

cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
cdf.head(9)

#viz = cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
#viz.hist()
#plt.show()

#plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS,  color='blue')
#plt.xlabel("FUELCONSUMPTION_COMB")
#plt.ylabel("Emission")
#plt.show()

#plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
#plt.xlabel("Engine size")
#plt.ylabel("Emission")
#plt.show()

msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

#plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
#plt.xlabel("Engine size")
#plt.ylabel("Emission")
#plt.show()

from sklearn import linear_model
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit (train_x, train_y)
# The coefficients
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)

from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_hat = regr.predict(test_x)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_hat - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_hat - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y_hat , test_y) )