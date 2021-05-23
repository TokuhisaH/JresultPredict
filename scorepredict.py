import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

#チーム情報読み込み
match_card=[]
with open('match_card.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        match_card.extend(row)

dataset_home = pd.read_csv('result_data_H.csv',header=None,encoding="shift-jis")
#ホームのクラブがどのクラブに対して何点取るか、という予想をするモデル
X_home = dataset_home.iloc[:, [0,5,6]].values
Y_home= dataset_home.iloc[:, 7:8].values

dataset_away = pd.read_csv('result_data_A.csv',header=None,encoding="shift-jis")
#アウェイのクラブがどのクラブに対して何点取るか、という予想をするモデル
X_away = dataset_away.iloc[:, [0,5,6]].values
Y_away = dataset_away.iloc[:, 7:8].values

print("data import clear")


#列のデータを変換するためのクラス
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

cd = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[1,2])],remainder="passthrough")
X_home=(cd.fit_transform(X_home)).toarray()
X_away=(cd.fit_transform(X_away)).toarray()

print("encoding clear")

#randomforestはensembleからimport
from sklearn.ensemble import  RandomForestRegressor
#n_estimatorsでいくつの木（モデル）に分割するか指定
regressor_home = RandomForestRegressor(n_estimators=10,random_state=0)
regressor_away = RandomForestRegressor(n_estimators=10,random_state=0)
regressor_home.fit(X_home,Y_home)
regressor_away.fit(X_away,Y_away)

print("learning clear")

#予想したい対戦カード
home_card=[[2021,match_card[0],match_card[1]]]
print(home_card)
away_card=[[home_card[0][0],home_card[0][2],home_card[0][1]]]

#予想スコア
home_score_predict=regressor_home.predict(cd.transform(home_card))
away_score_predict=regressor_away.predict(cd.transform(away_card))

#データアウトプット
with open('score_predict.csv', 'w',newline='') as f:
    writer = csv.writer(f,lineterminator=',')
    writer.writerows([["2021"],[match_card[0]],[match_card[1]],home_score_predict,away_score_predict])

print("Score Predict Complete!")