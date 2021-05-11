import tkinter as tk
from tkinter import ttk
import sys
import subprocess


#検索対象チーム
OptionList = [
"浦和",
"名古屋",
"FC東京",
"Ｇ大阪"
] 
home=""
away=""

class Set_card_class(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.home_team = tk.StringVar()
        self.away_team = tk.StringVar()
        self.label=tk.Label(self,text="チームを選択してください")
        self.label.pack()
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.combo = ttk.Combobox(self,text="ホームクラブ",values=OptionList,textvariable=self.home_team)
        self.combo.pack(side = 'left')
        self.label=tk.Label(self,text="　VS　")
        self.label.pack(side = 'left')
        self.combo = ttk.Combobox(self,values=OptionList,textvariable=self.away_team)
        self.combo.pack(side = 'top')
        # button = ttk.Button(self,text="print",command= self.TeamSet)
        # button.pack()
    
    def TeamSet(self):
         home=self.home_team.get()
         away=self.away_team.get()

        # print(self.home_team.get())
        # print(self.away_team.get())
        # print(self.combo.get())

if __name__ == '__main__':
    #ウィンドウ生成
    root = tk.Tk()
    root.title(u"操作メニュー")
    root.geometry("480x340")
    Set_card_class(root)

    #ボタン一覧
    def scraping():
        subprocess.Popen(r'python scraping.py')

    def datatransform():
        subprocess.Popen(r'C:\Users\tokuh\Documents\Products\JresultPredict\DataTransform.py')

    def scorepredict():
        subprocess.Popen(r'C:\Users\tokuh\Documents\Products\JresultPredict\scorepredict.py')

    def resultpredict():
        subprocess.Popen(r'C:\Users\tokuh\Documents\Products\JresultPredict\resultpredict.py')

    def finish_menu():
        sys.exit()


    # # スクレイピング
    # labeltitle = tk.Label(root, text=u'■■■操作メニュー■■■')
    # labeltitle.pack()
    # Label_Blanc = tk.Label(root, text=u'')
    # Label_Blanc.pack()
    # scraping_Button = tk.Button(root, text=u'データ収集', width=30)
    # scraping_Button["command"] = scraping
    # scraping_Button.pack()

    # # データ変形
    # Label_Blanc = tk.Label(root, text=u'')
    # Label_Blanc.pack()
    # datatransform_Button = tk.Button(root, text=u'プログラム２', width=30)
    # datatransform_Button["command"] = datatransform
    # datatransform_Button.pack()

    # # スコア予想
    # Label_Blanc = tk.Label(root, text=u'')
    # Label_Blanc.pack()
    # scorepredict_Button = tk.Button(root, text=u'プログラム３', width=30)
    # scorepredict_Button["command"] = scorepredict
    # scorepredict_Button.pack()

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