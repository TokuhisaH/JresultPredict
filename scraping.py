from bs4 import BeautifulSoup as bs
import requests

#取得するシーズン
competition_years="2010"
competition_frame_ids=1

#URL
link="https://data.j-league.or.jp/SFMS01/search?competition_years="+competition_years+"&competition_frame_ids="+str(competition_frame_ids)

#取得
site = requests.get(link)
soup=bs(site.text,"html.parser")

#タグから情報を絞り込み
table=soup.body.find_all("tbody")[0]
games=table.find_all("tr")

#まとめるリスト定義
results_data=[]

#リストにまとめる
for game in games:
    row = []
    for cell in game.find_all("td"):
        row.append(cell.get_text(strip=True))
    
    results_data.append(row)

print(results_data)