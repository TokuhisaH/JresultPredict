import tkinter as tk
from tkinter import ttk
import sys
import subprocess
import csv


#検索対象チーム
OptionList = [
"浦和",
"名古屋",
"FC東京",
"Ｇ大阪"
] 

#ウィンドウ生成
root = tk.Tk()
root.geometry('400x300')

#Widget変数

labeltitle = tk.Label(root, text=u'■■■操作メニュー■■■')
labeltitle.pack()

tk_hometeam=tk.StringVar()
hometeam_combo=ttk.Combobox(values=OptionList,textvariable=tk_hometeam)
hometeam_combo.pack()

labeltitle = tk.Label(root, text=u'VS')
labeltitle.pack()

tk_awayteam=tk.StringVar()
awayteam_combo=ttk.Combobox(values=OptionList,textvariable=tk_awayteam)
awayteam_combo.pack()

#空白行
Label_Blanc = tk.Label(root, text=u'')
Label_Blanc.pack()

#値の取得
match_card=[]
def setCard():
    hometeam=tk_hometeam.get()
    awayteam=tk_awayteam.get()
    match_card=[[hometeam],[awayteam]]
    # combo.get()
    print(match_card)
    with open('import_data.csv', 'w') as f:
        writer = csv.writer(f,lineterminator='\n')
        writer.writerows(match_card)


def scraping():
    subprocess.Popen(r'python scraping.py')
    subprocess.Popen(r'python DataTransform.py')

# def datatransform():
#     subprocess.Popen(r'C:\Users\tokuh\Documents\Products\JresultPredict\DataTransform.py')

def scorepredict():
    subprocess.Popen(r'python scorepredict.py')

def resultpredict():
    subprocess.Popen(r'C:\Users\tokuh\Documents\Products\JresultPredict\resultpredict.py')

def finish_menu():
    sys.exit()

#ボタン一覧
hometeam_Button = tk.Button(root, text=u'対戦カード決定', width=10)
hometeam_Button["command"] = setCard
hometeam_Button.pack()

#空白行
Label_Blanc = tk.Label(root, text=u'')
Label_Blanc.pack()

# スクレイピング
scraping_Button = tk.Button(root, text=u'データ収集', width=10)
scraping_Button["command"] = scraping
scraping_Button.pack()

# # データ変形
# Label_Blanc = tk.Label(root, text=u'')
# Label_Blanc.pack()
# datatransform_Button = tk.Button(root, text=u'プログラム２', width=30)
# datatransform_Button["command"] = datatransform
# datatransform_Button.pack()

# スコア予想
Label_Blanc = tk.Label(root, text=u'')
Label_Blanc.pack()
scorepredict_Button = tk.Button(root, text=u'スコア予想', width=10)
scorepredict_Button["command"] = scorepredict
scorepredict_Button.pack()

# # 結果予想
# Label_Blanc = tk.Label(root, text=u'')
# Label_Blanc.pack()
# resultpredict_Button = tk.Button(root, text=u'プログラム３', width=30)
# resultpredict_Button["command"] = resultpredict
# resultpredict_Button.pack()

# 終了
Label_Blanc = tk.Label(root, text=u'')
Label_Blanc.pack()
finish_menu_Button = tk.Button(root, text=u'終了')
finish_menu_Button["command"] = finish_menu
finish_menu_Button.pack()

root.mainloop()