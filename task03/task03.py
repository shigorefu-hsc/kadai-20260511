import pandas as pd


df = pd.read_csv("hotel_guests.csv")


while True:
    print("\n=== task03: ホテル宿泊者データの条件抽出 ===")
    print("1. 指定した国の宿泊者を表示する")
    print("2. 指定した日数以上宿泊した人を表示する")
    print("3. 指定した金額以上を払った人を表示する")
    print("4. 国と宿泊日数の2つの条件で絞り込む")
    print("5. 朝食付きの予約だけを表示する")
    print("6. 必要な列だけを表示する")
    print("0. 終了")

    choice = input("番号を選んでください: ")

    if choice == "1":
        country = input("国を入力してください: ")
        # TODO: 国が country と同じ行だけを表示する
        pass
    elif choice == "2":
        days = int(input("宿泊日数の最小値: "))
        # TODO: 宿泊日数が days 以上の行だけを表示する
        pass
    elif choice == "3":
        price = int(input("宿泊料金の最小値: "))
        # TODO: 宿泊料金が price 以上の行だけを表示する
        pass
    elif choice == "4":
        country = input("国を入力してください: ")
        days = int(input("宿泊日数の最小値: "))
        # TODO: 国が country かつ 宿泊日数が days 以上の行を表示する
        # TODO: 複数条件では & と () を使う
        pass
    elif choice == "5":
        # TODO: 朝食 が "あり" の行だけを表示する
        pass
    elif choice == "6":
        # TODO: 名前、国、宿泊日数、宿泊料金だけを表示する
        pass
    elif choice == "0":
        break
    else:
        print("その番号はありません")
