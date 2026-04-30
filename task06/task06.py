import pandas as pd


df = pd.read_csv("school_scores.csv")


while True:
    print("\n=== task06: groupbyで学科ごとに集計する ===")
    print("1. 学科ごとの平均成績を表示する")
    print("2. 学科ごとの平均出席率を表示する")
    print("3. 学科ごとの学生数を表示する")
    print("4. 学科ごとの学費合計を表示する")
    print("5. キャンパスと性別ごとの平均出席率を表示する")
    print("6. 出身地ごとの学生名リストを表示する")
    print("0. 終了")

    choice = input("番号を選んでください: ")

    if choice == "1":
        # TODO: groupby("学科")["成績"].mean() を使う
        pass
    elif choice == "2":
        # TODO: groupby("学科")["出席率"].mean() を使う
        pass
    elif choice == "3":
        # TODO: groupby("学科")["名前"].count() を使う
        pass
    elif choice == "4":
        # TODO: groupby("学科")["学費"].sum() を使う
        pass
    elif choice == "5":
        # TODO: groupby(["キャンパス", "性別"])["出席率"].mean() を使う
        pass
    elif choice == "6":
        # TODO: groupby("出身地")["名前"].apply(list) を使う
        pass
    elif choice == "0":
        break
    else:
        print("その番号はありません")
