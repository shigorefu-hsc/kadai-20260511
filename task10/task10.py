import pandas as pd


df = pd.read_csv("dirty_sales.csv")


while True:
    print("\n=== task10: 汚いCSVをきれいにする最終課題 ===")
    print("1. 最初の5行を表示する")
    print("2. 行数・列数・列名・データ型を確認する")
    print("3. 欠損値の数を確認する")
    print("4. 数値に変換する")
    print("5. 不要な列を削除する")
    print("6. 列名を英語に変更する")
    print("7. 合計金額を計算して新しい列を作る")
    print("8. cleaned_sales.csv に保存する")
    print("9. 現在の表を表示する")
    print("0. 終了")

    choice = input("番号を選んでください: ")

    if choice == "1":
        # TODO: df.head() を表示する
        pass
    elif choice == "2":
        # TODO: df.shape, df.columns, df.dtypes を表示する
        pass
    elif choice == "3":
        # TODO: df.isna().sum() を表示する
        pass
    elif choice == "4":
        # TODO: 数量、単価、割引額を pd.to_numeric() で数値に変換する
        # errors="coerce" を指定する
        pass
    elif choice == "5":
        # TODO: メモ列を削除する
        # ヒント: df = df.drop(columns=["メモ"])
        pass
    elif choice == "6":
        # TODO: rename() を使って列名を英語に変更する
        # 例: 注文ID -> order_id, 商品名 -> product_name
        pass
    elif choice == "7":
        # TODO: 合計金額 = 数量 * 単価 - 割引額 の列を作る
        # 列名を変更した後なら英語の列名を使う
        # 列名を変更する前なら日本語の列名を使う
        pass
    elif choice == "8":
        # TODO: df を cleaned_sales.csv として保存する
        # index=False, encoding="utf-8-sig" を指定する
        pass
    elif choice == "9":
        print(df)
    elif choice == "0":
        break
    else:
        print("その番号はありません")
