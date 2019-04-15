# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:14:30 2019

@author: lenovo
"""

SIMPLE LINEAR REGRESSION


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Income_Data.csv')

features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2,
                   random_state = 0)



# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(features, labels)

regressor.predict(6.5)


# Predicting the Test set results
labels_pred = regressor.predict(features_test)

print (regressor.predict(6.5))

# Visualising the Training set results
plt.scatter(features_train, labels_train, color = 'red')
plt.plot(features_train, regressor.predict(features_train), color = 'blue')
plt.title('Income vs ML-Experience (Training set)')
plt.xlabel('ML-Experience')
plt.ylabel('Income')
plt.show()


# Visualising the Test set results
#plt.scatter(features_train, labels_train, color = 'green')
plt.scatter(features_test, labels_test, color = 'red')
plt.plot(features_train, regressor.predict(features_train), color = 'blue')
plt.title('Income vs ML-Experience (Test set)')
plt.xlabel('ML-Experience')
plt.ylabel('Income')
plt.show()



#Model accuracy
print (regressor.score(features_test, labels_test))
print (regressor.score(features_train, labels_train))


CODE CHALLENGES

Q1. (Create a program that fulfills the following specification.)
Foodtruck.csv


You will implement linear regression to predict the profits for a food chain company.

Case: Suppose you are the CEO of a restaurant franchise and are considering 
different cities for opening a new outlet. 
The chain already has food-trucks in various cities and you have data for profits 
and populations from the cities. 
You would like to use this data to help you select which city to expand to next. 

Foodtruck.csv contains the dataset for our linear regression problem. 
The first column is the population of a city and the second column is the 
profit of a food truck in that city. 
A negative value for profit indicates a loss.

Perform Simple Linear regression to predict the profit based on the population 
observed and visualize the result.
Based on the above trained results, what will be your estimated profit, 
if you set up your outlet in Jaipur? (Current population in Jaipur is 3.073 million)



Q2. (Create a program that fulfills the following specification.)

Import Bahubali2vsDangal.csv file.

It contains Data of Day wise collections of the movies Bahubali 2 and Dangal (in crores) for the first 9 days.
Now, you have to write a python code to predict which movie would collect more on the 10th day.


MULTIPLE LINEAR REGRESSION

# Multiple Linear Regression

# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Classification.csv')
temp = dataset.values 
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder() 
features[:, 0] = labelencoder.fit_transform(features[:, 0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()

# Avoiding the Dummy Variable Trap
features = features[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)  

# Predicting the Test set results
Pred = regressor.predict(features_test)
x = [0,0,1150,3,4]
x = np.array(x)
regressor.predict(x.reshape(1, -1))





# Getting Score for the Multi Linear Reg model
Score = regressor.score(features_train, labels_train)
Score = regressor.score(features_test, labels_test)

# Predicting for some other values
x = np.array([0,  0,1150, 3,  4]).reshape(1,-1)

print (regressor.predict(x))
print (regressor.coef_)













# Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
#This is done because statsmodels library requires it to be done for constants.
features = np.append(arr = np.ones((30, 1)), values = features, axis = 1)








features_opt = features[:, [0, 1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()





features_opt = features[:, [0, 1, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = labels, exog = features).fit()
regressor_OLS.summary()





features_opt = features[:, [0, 1, 3, 5]]
regressor_OLS = sm.OLS(endog = labels, exog = features).fit()
regressor_OLS.summary()




features_opt = features[:, [0, 3, 5]]
regressor_OLS = sm.OLS(endog = labels, exog = features).fit()
regressor_OLS.summary()



features_opt = features[:, [0, 5]]
regressor_OLS = sm.OLS(endog = labels, exog = features).fit()
print regressor_OLS.summary()


CODE CHALLENGES


Q1. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.






POLYNOMIAL REGRESSION


# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
features = dataset.iloc[:, 1:2].values
labels = dataset.iloc[:, 2].values


# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(features, labels)

print ("Predicting result with Linear Regression",)
print (lin_reg.predict(6.5))

#print the scores
print (lin_reg.score(features, labels))
#if the score is poor, it seems we are using a very simple model that does 
#not fit the data well. May be a case of underfitting


# Visualising the Linear Regression results



# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
# create the polynomial features using above class
poln_object = PolynomialFeatures(degree = 6)

features_poln = poln_object.fit_transform(features)
#poln_object.fit(features_poln)

#once you have the poln_matrix read, input it to linear regressor
lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poln, labels)




print ("Predicting result with Polynomial Regression",)
#need to convert 6.5 into polynomial features
#poln_object.fit_transform(6.5)
#pd.DataFrame(poln_object.fit_transform(6.5))

print (lin_reg_2.predict(poln_object.fit_transform(6.5)))



# Visualising the Polynomial Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poln_object.fit_transform(features)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#evaluate the score
#you will have to convert features to polynomial matrix and then get the score
lin_reg_2.score(poln_object.fit_transform(features), labels)




# Visualising the Polynomial Regression results (for higher resolution and smoother curve)
features_grid = np.arange(min(features), max(features), 0.1)
features_grid = features_grid.reshape((-1, 1))
plt.scatter(features, labels, color = 'red')
plt.plot(features_grid, lin_reg_2.predict(poln_object.fit_transform(features_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

CODE CHALLENGE


Q1. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking into account a quadratic function of the age of the fish.






LOGISTIC REGRESSION
# Logistic Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
features = dataset.iloc[:, [2, 3]].values
labels = dataset.iloc[:, 4].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)                                    

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Visualising the Training set results
from matplotlib.colors import ListedColormap
features_set, labels_set = features_train, labels_train
features1, features2 = np.meshgrid(np.arange(start = features_set[:, 0].min() - 1, stop = features_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = features_set[:, 1].min() - 1, stop = features_set[:, 1].max() + 1, step = 0.01))
plt.contourf(features1, features2, classifier.predict(np.array([features1.ravel(), features2.ravel()]).T).reshape(features1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(features1.min(), features1.max())
plt.ylim(features2.min(), features2.max())
for i, j in enumerate(np.unique(labels_set)):
    plt.scatter(features_set[labels_set == j, 0], features_set[labels_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

# Visualising the Test set results
from matplotlib.colors import ListedColormap
features_set, labels_set = features_test, labels_test
features1, features2 = np.meshgrid(np.arange(start = features_set[:, 0].min() - 1, stop = features_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = features_set[:, 1].min() - 1, stop = features_set[:, 1].max() + 1, step = 0.01))
plt.contourf(features1, features2, classifier.predict(np.array([features1.ravel(), features2.ravel()]).T).reshape(features1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(features1.min(), features1.max())
plt.ylim(features2.min(), features2.max())
for i, j in enumerate(np.unique(labels_set)):
    plt.scatter(features_set[labels_set == j, 0], features_set[labels_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

CODE CHALLENGE

Q1. (Create a program that fulfills the following specification.)
affairs.csv


Import the affairs.csv file.

It was derived from a survey of women in 1974 by Redbook magazine, in which
 married women were asked about their participation in extramarital affairs.

Description of Variables

The dataset contains 6366 observations of 10 variables:(modified and cleaned)

rate_marriage: woman's rating of her marriage (1 = very poor, 5 = very good)

age: women's age

yrs_married: number of years married

children: number of children

religious: women's rating of how religious she is (1 = not religious, 4 = strongly religious)

educ: level of education (9 = grade school, 12 = high school, 14 = some college, 
                          16 = college graduate, 17 = some graduate school, 20 = advanced degree)

occupation: women's occupation (1 = student, 2 = farming/semi-skilled/unskilled, 3 = "white collar",
 4 = teacher/nurse/writer/technician/skilled, 5 = managerial/business, 6 = professional with advanced degree)

occupation_husb: husband's occupation (same coding as above)

affair: outcome 0/1, where 1 means a woman had at least 1 affair.

    Now, perform Classification using logistic regression and check your model 
    accuracy using confusion matrix and also through .score() function.

NOTE: Perform OneHotEncoding for occupation and occupation_husb, since they should
 be treated as categorical variables. Careful from dummy variable trap for both!!

    What percentage of total women actually had an affair?

(note that Increases in marriage rating and religiousness correspond to a decrease
 in the likelihood of having an affair.)

    Predict the probability of an affair for a random woman not present in the dataset.
    She's a 25-year-old teacher who graduated college, has been married for 3 years, has 1 child, 
    rates herself as strongly religious, rates her marriage as fair, and her husband is a farmer.

Optional

    Build an optimum model, observe all the coefficients.