from bs4 import BeautifulSoup as bs
import requests
import re
import csv
import pprint

#取得するシーズン
competition_years=[]

#Jリーグ開幕から28年の28
y=1993
for i in range(29):
    competition_years.append(str(y+i))

competition_frame_ids=1

#試合結果まとめるリスト定義
results_data=[]

for i in range(len(competition_years)):
    #URL
    link="https://data.j-league.or.jp/SFMS01/search?competition_years="+competition_years[i]+"&competition_frame_ids="+str(competition_frame_ids)
  
    #取得
    site = requests.get(link)
    soup=bs(site.text,"html.parser")

    #タグから情報を絞り込み
    table=soup.body.find_all("tbody")[0]
    games=table.find_all("tr")

    #リストにまとめる
    for game in games:
        match_score=[]
        row = []
        for cell in game.find_all("td"):
            #セルから余計な情報を削除
            cell=cell.get_text(strip=True)
            #正規表現でスコアを別カラムに
            row.append(cell)
        try:
            match_score=re.findall(r"\d+",row[6])
            del row[6]
            row.insert(6,match_score[0])
            row.insert(8,match_score[1])
            print(row)
        except IndexError:
            print(row)
            break
        results_data.append(row)

#csv出力
with open('result_data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(results_data)

print("complete!")