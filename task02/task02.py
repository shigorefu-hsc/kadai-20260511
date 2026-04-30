import pandas as pd


df = pd.read_csv("tourists.csv")


while True:
    print("\n=== task02: 観光客データの分析 ===")
    print("1. 全ての観光客の平均年齢を表示する")
    print("2. 観光客が一番多い国を表示する")
    print("3. 使用金額の最大値を表示する")
    print("4. 使用金額が一番多い観光客の情報を表示する")
    print("5. 平均滞在日数を表示する")
    print("6. 指定した金額以上を使った観光客を表示する")
    print("7. データの最初の5行を表示する")
    print("0. 終了")

    choice = input("番号を選んでください: ")

    if choice == "1":
        # TODO: 年齢の平均を計算して表示する
        pass
    elif choice == "2":
        # TODO: value_counts() を使って、一番人数が多い国を表示する
        pass
    elif choice == "3":
        # TODO: 使用金額の最大値を表示する
        pass
    elif choice == "4":
        # TODO: 使用金額が最大の観光客の行を表示する
        pass
    elif choice == "5":
        # TODO: 滞在日数の平均を計算して表示する
        pass
    elif choice == "6":
        amount = int(input("使用金額の最小値を入力してください: "))
        # TODO: 使用金額が amount 以上の観光客だけを表示する
        pass
    elif choice == "7":
        # TODO: 最初の5行を表示する
        pass
    elif choice == "0":
        break
    else:
        print("その番号はありません")
