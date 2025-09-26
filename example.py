from pathlib import Path
import os

# 相対パスを絶対パスに変換
relative_path = "./data/example.txt"
absolute_path = Path(relative_path).resolve()

print("絶対パス:", absolute_path)

os.makedirs("./data1/", exist_ok=True)