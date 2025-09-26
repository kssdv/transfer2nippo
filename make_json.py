import json

data = {
    "name" : "キム・サンシン",
    "month_goal" : ["・PaizaのAランク達成","・個人プロジェクトの目標設定と開始、九月末までに完成"]
}

# JSONファイルに書き込む
with open("./data/data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("JSONファイルが作成されました！")