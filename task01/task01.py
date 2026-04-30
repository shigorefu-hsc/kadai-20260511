import pandas as pd

df = pd.read_csv("students.csv")

while True:
    print("\n=== task01: データを見るメニュー ===")
    print("1. 最初の行を表示する")
    print("2. 最後の行を表示する")
    print("3. 全てのデータを表示する")
    print("4. 行数と列数を表示する")
    print("0. 終了")

    choice = input("番号を選んでください: ")

    if choice == "1":
        count = ask_number("最初から何行表示しますか？ ")
        # TODO: DataFrame の最初の count 行を表示する
        pass
    elif choice == "2":
        count = ask_number("最後から何行表示しますか？ ")
        # TODO: DataFrame の最後の count 行を表示する
        pass
    elif choice == "3":
        # TODO: DataFrame 全体を表示する
        pass
    elif choice == "4":
        # TODO: df.shape を使って行数と列数を表示する
        pass
    elif choice == "0":
        print("終了します")
        break
    else:
