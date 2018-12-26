import pickle
import pandas as pd
test_data_location="D:///test_dvc//Demo//DataVersioning//data//LogisticRegressionData//testing.csv"
model_location="D:///test_dvc//Demo//DataVersioning//model//LogisticRegressionModel//lr"
data=pd.read_csv(test_data_location)
lr_model = open(model_location, 'rb')
lr_object = pickle.load(lr_model)
predictions = lr_object.predict(data)
print(predictions)



