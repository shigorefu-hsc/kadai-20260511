import pandas as pd


df = pd.read_csv("orders.csv")


while True:
    print("\n=== task05: 注文データの基本集計 ===")
    print("1. 注文数を表示する")
    print("2. 合計金額の合計を表示する")
    print("3. 合計金額の平均を表示する")
    print("4. 一番多い支払方法を表示する")
    print("5. 商品カテゴリごとの注文数を表示する")
    print("6. 購入者地域ごとの注文数を表示する")
    print("7. 合計金額が最大の注文を表示する")
    print("0. 終了")

    choice = input("番号を選んでください: ")

    if choice == "1":
        # TODO: count() または len(df) を使って注文数を表示する
        pass
    elif choice == "2":
        # TODO: 合計金額の合計を表示する
        pass
    elif choice == "3":
        # TODO: 合計金額の平均を表示する
        pass
    elif choice == "4":
        # TODO: 支払方法に value_counts() を使う
        # TODO: 一番多い支払方法を表示する
        pass
    elif choice == "5":
        # TODO: 商品カテゴリに value_counts() を使って表示する
        pass
    elif choice == "6":
        # TODO: 購入者地域に value_counts() を使って表示する
        pass
    elif choice == "7":
        # TODO: 合計金額が最大の注文の行を表示する
        pass
    elif choice == "0":
        break
    else:
        print("その番号はありません")
