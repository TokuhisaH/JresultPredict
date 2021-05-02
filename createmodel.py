import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset_home = pd.read_csv('result_data_H.csv',header=None,encoding="shift-jis")
#ホームのクラブがどのクラブに対して何点取るか、という予想をするモデル
# X_home = dataset_home.iloc[:, [0,5,6]].values
X_home = dataset_home.iloc[:, 5:7].values
Y_home = dataset_home.iloc[:, 7:8].values

dataset_away = pd.read_csv('result_data_A.csv',header=None,encoding="shift-jis")
#アウェイのクラブがどのクラブに対して何点取るか、という予想をするモデル
X_away = dataset_away.iloc[:, 5:7].values
Y_away = dataset_away.iloc[:, 7:8].values

#one-hotエンコーディング
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder

transformer_home = OneHotEncoder().fit(X_home)
transformer_away = OneHotEncoder().fit(X_away)

# print(transformer_home.transform(X_home).toarray()[0])
X_home=transformer_home.transform(X_home).toarray()
X_away=transformer_away.transform(X_away).toarray()

#randomforestはensembleからimport
from sklearn.ensemble import  RandomForestRegressor
#n_estimatorsでいくつの木（モデル）に分割するか指定
regressor_home = RandomForestRegressor(n_estimators=10,random_state=0)
regressor_away = RandomForestRegressor(n_estimators=10,random_state=0)
regressor_home.fit(X_train_home,Y_train_home)
regressor_away.fit(X_train_away,Y_train_away)

print(regressor_home.predict(transformer_home.transform([["Ｃ大阪","Ｇ大阪"]])))
print(regressor_away.predict(transformer_away.transform([["Ｇ大阪","Ｃ大阪"]])))