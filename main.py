from dotenv import load_dotenv
import os
from read_excel import read_excel
from pathlib import Path

load_dotenv()

YOUR_NAME = os.getenv("YOUR_NAME")
file_name = f"業務日報_202510_{YOUR_NAME}.xlsx"
# file_name = "FILE_NAME.xlsx"

# Downloadsフォルダー
path = str(Path.home() / "Downloads")
path = path+f"\\{file_name}"
data = read_excel(path)

name = YOUR_NAME

# 書き込みする.txtファイル名
txt_path = "./data/日報.txt"

# フォルダが存在しない場合に作成
os.makedirs("./data/", exist_ok=True)

# テキストファイルの作成または修正
with open(txt_path, "w", encoding="utf-8") as file:
    file.write(f"【名前】\n{name}\n\n")
    # print(data)
    for i in data[0]:
        # 時刻とやったことが空白区切りで分かれているため、空白基準でsplit()
        # ex) 09:10～12:00　業務内容 => ['09:10～12:00', '業務内容']
        tmp = i.split("　")
        if(len(tmp) >= 2):
            file.write(f"{tmp[0]}\n")
            file.write(f"{tmp[-1]}\n")
            file.write("\n")
        else:
            file.write(f"{i}\n")
        # file.write("\n")

    for i in data[1]:
        file.write(f"{i}\n")
    file.write("\n")

    # 明日の目標
    file.write("【明日の学習目標】\n")
    file.write("・\n")
    file.write("・\n")
    file.write("\n")
    
    # 月間目標
    file.write(f"【十月までの目標】\n")
    file.write("・PaizaのSランク達成\n")
    file.write("・Javaの「Sランク獲得」問題を全部解く\n")

