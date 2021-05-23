import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scorepredict

#対戦カードとスコアを独立変数に、勝敗結果を予想
X_home = scorepredict.dataset_home.iloc[:, [0,5,6,7,8]].values
Y_home = scorepredict.dataset_home.iloc[:, [11]].values

#アウェイ版 今回はいらないかも（ホームの結果がわかればアウェイの結果もわかるので）
X_away = scorepredict.dataset_away.iloc[:, [0,5,6,7,8]].values
Y_away = scorepredict.dataset_away.iloc[:, [11]].values

#列のデータを変換するためのクラス
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

cd = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[1,2])],remainder="passthrough")
X_home=(cd.fit_transform(X_home)).toarray()

#目的変数のone-hotエンコーディング
transformer_Y= OneHotEncoder().fit(Y_home)
Y_home=transformer_Y.transform(Y_home).toarray()

#訓練とテストに分割
from sklearn.model_selection import train_test_split
X_home_train, X_home_test, Y_home_train, Y_home_test = train_test_split(X_home, Y_home, test_size = 0.25, random_state = 0)

#訓練データで学習
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)

classifier.fit(X_home_train, Y_home_train)

#予想したいカード
scorepredict.home_card[0].append(scorepredict.home_score_predict[0])
scorepredict.home_card[0].append(scorepredict.away_score_predict[0])
print(scorepredict.home_card)
Predict_card=cd.transform(scorepredict.home_card)

#予想結果
print(transformer_Y.inverse_transform(classifier.predict(Predict_card.toarray())))

#テストデータでモデルの精度評価
# Y_pred = (classifier.predict(X_home_test))
# Y_pred=transformer_Y.inverse_transform(Y_pred)
# Y_home_test=transformer_Y.inverse_transform(Y_home_test)
# print(np.concatenate((Y_pred.reshape(len(Y_pred),1), Y_home_test.reshape(len(Y_home_test),1)),1))

# #混同行列の作成
# from sklearn.metrics import confusion_matrix, accuracy_score
# cm = confusion_matrix(Y_home_test, Y_pred)
# print(cm)
# accuracy_score(Y_home_test, Y_pred)