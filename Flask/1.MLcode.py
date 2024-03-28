from sklearn.datasets import load_iris
iris = load_iris()
iris_data = iris['data']
iris_target = iris['target']
target_names = iris['target_names']
feature_names = iris['feature_names']

from sklearn.model_selection import train_test_split
# split the data into training and test
iris_data_train, iris_data_test, iris_target_train, iris_target_test = train_test_split(iris_data, iris_target)
#iris_data_train.shape, iris_data_test.shape, iris_target_train.shape, iris_target_test.shape
# fit the model
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression().fit(iris_data_train, iris_target_train)
# evaluate model performance
from sklearn.metrics import confusion_matrix
iris_target_test_pred = lr.predict(iris_data_test)
confusion_matrix(iris_target_test, iris_target_test_pred)

import pickle
with open('iris_logistic_regression.pkl','wb') as f:
    pickle.dump(lr,f)
