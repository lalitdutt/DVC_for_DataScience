import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

#config
data_location = "D:///test_dvc//Demo//DataVersioning//data//LogisticRegressionData//diabetes.csv"
model_location="D:///test_dvc//Demo//DataVersioning//model//LogisticRegressionModel//"
training_data="D:///test_dvc//Demo//DataVersioning//data//LogisticRegressionData//training.csv"
test_data="D:///test_dvc//Demo//DataVersioning//data//LogisticRegressionData//testing.csv"

#Load Data
data=pd.read_csv(data_location)

#Data Prep
cols = ['Pregnancies','Glucose','DiabetesPedigreeFunction','Insulin','BMI','Age']
Y=data['Outcome']
X=data[cols]
X_train,X_test,Y_train,Y_test = train_test_split(X,Y, random_state = 25, test_size = 0.2)
X_train.to_csv(training_data,index=False)
X_test.to_csv(test_data,index=False)

#Model Training
lr = LogisticRegression()
lr.fit(X_train,Y_train)

#Model Persisting
model_pickle = open(model_location+'lr', 'ab')
pickle.dump(lr, model_pickle)
model_pickle.close()
