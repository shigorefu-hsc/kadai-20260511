import pandas as pd


df = pd.read_csv("employees.csv")


while True:
    print("\n=== task07: 給与データを計算してCSVに保存する ===")
    print("1. 残業代を計算する")
    print("2. 総支給額を計算する")
    print("3. 評価結果を追加する")
    print("4. 必要な列だけを表示する")
    print("5. result.csv に保存する")
    print("6. 現在の表を表示する")
    print("0. 終了")

    choice = input("番号を選んでください: ")

    if choice == "1":
        # TODO: 残業代 = 残業時間 * 時給 の列を作る
        # 列名は "残業代" にする
        pass
    elif choice == "2":
        # TODO: 総支給額 = 基本給 + 残業代 + ボーナス の列を作る
        # 残業代の列がまだない場合は、先に残業代を作る
        pass
    elif choice == "3":
        # TODO: apply() を使って 評価結果 の列を作る
        # 評価点が90以上なら "優秀"
        # 評価点が70以上なら "普通"
        # それ以外なら "要改善"
        pass
    elif choice == "4":
        # TODO: 名前、部署、基本給、残業代、ボーナス、総支給額、評価結果だけを表示する
        pass
    elif choice == "5":
        # TODO: df を result.csv として保存する
        # index=False, encoding="utf-8-sig" を指定する
        pass
    elif choice == "6":
        print(df)
        pass
    elif choice == "0":
        break
    else:
        print("その番号はありません")
