import json
import pandas as pd

players = []

for i in range(1, 21):
    file_name = f"players/player_{i:02}.json"

    with open(file_name, "r", encoding="utf-8") as file:
        player = json.load(file)

    players.append(player)

df = pd.DataFrame(players)

while True:
    print("\n=== task08: プレイヤーJSONを1つの表にまとめる ===")
    print("1. 現在の表を表示する")
    print("2. 最大レベルとの差を追加する")
    print("3. players_result.csv に保存する")
    print("4. result.txt を作成する")
    print("5. 最初の5行を表示する")
    print("0. 終了")

    choice = input("番号を選んでください: ")

    if choice == "1":
        print(df)
        pass
    elif choice == "2":
        # TODO: レベル の最大値を求める
        # TODO: 最大レベルとの差 = 最大レベル - レベル の列を作る
        pass
    elif choice == "3":
        # TODO: df を players_result.csv として保存する
        # index=False, encoding="utf-8-sig" を指定する
        pass
    elif choice == "4":
        # TODO: result.txt を作成して、次の情報を書き込む
        # 1. 全プレイヤーの平均プレイ時間
        # 2. 全プレイヤー数
        # 3. ギルド数
        # 4. クラスごとのゴールド合計
        pass
    elif choice == "5":
        # TODO: df.head() を使って最初の5行を表示する
        pass
    elif choice == "0":
        break
    else:
        print("その番号はありません")
