import pandas as pd


df = pd.read_csv("products.csv")


while True:
    print("\n=== task04: 商品データの並び替え ===")
    print("1. 価格が安い順に並び替える")
    print("2. 価格が高い順に並び替える")
    print("3. 売上数が多い順に並び替える")
    print("4. 評価が高い商品トップ N を表示する")
    print("5. 在庫数が少ない商品トップ N を表示する")
    print("6. 指定したカテゴリの商品を価格順で表示する")
    print("0. 終了")

    choice = input("番号を選んでください: ")

    if choice == "1":
        # TODO: 価格を基準に昇順で並び替えて表示する
        pass
    elif choice == "2":
        # TODO: 価格を基準に降順で並び替えて表示する
        pass
    elif choice == "3":
        # TODO: 売上数を基準に降順で並び替えて表示する
        pass
    elif choice == "4":
        count = int(input("何件表示しますか？ "))
        # TODO: 評価を基準に降順で並び替えて、最初の count 行を表示する
        pass
    elif choice == "5":
        count = int(input("何件表示しますか？ "))
        # TODO: 在庫数を基準に昇順で並び替えて、最初の count 行を表示する
        pass
    elif choice == "6":
        category = input("カテゴリを入力してください: ")
        # TODO: 指定したカテゴリだけに絞り込む
        # TODO: その結果を価格の昇順で並び替えて表示する
        pass
    elif choice == "0":
        break
    else:
        print("その番号はありません")
