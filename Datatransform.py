#データをホーム目線、アウェイ目線の２パターン作る
import csv
import pprint
import copy
import numpy as np

home_data=[]
with open("result_data.csv", "r")as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row)==0:
            pass
        else:
            home_data.append(row)

# 一度ホームデータの中身をコピーし、そのあとに中の要素を入れ替える
away_data=[]
away_data=copy.deepcopy(home_data)
i=0
for i in range(len(away_data)):
    away_data[i][5],away_data[i][6]=home_data[i][7],home_data[i][8]
    away_data[i][7],away_data[i][8]=home_data[i][5],home_data[i][6]

result_data_H_A=[]

#extendで結合すると入れ子にならない
result_data_H_A.extend(home_data)
result_data_H_A.extend(away_data)

#ソートする
result_data_H_A=sorted(result_data_H_A,key=lambda x:(x[1],x[3],x[4]), reverse=True)

#csv出力
with open('result_data_H_A.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(result_data_H_A)
    

