import sqlite3
import pandas as pd


DB_FILE = "school.db"


def show_tables(conn):
    # TODO: sqlite_master からテーブル名の一覧を取得する
    # ヒント:
    # query = "SELECT name FROM sqlite_master WHERE type='table'"
    # tables = pd.read_sql_query(query, conn)
    # print(tables)
    pass


while True:
    print("\n=== task09: SQLデータをpandasで読み込む ===")
    print("1. テーブル一覧を表示する")
    print("2. テーブル名を入力してデータを表示する")
    print("0. 終了")

    choice = input("番号を選んでください: ")

    with sqlite3.connect(DB_FILE) as conn:
        if choice == "1":
            show_tables(conn)
        elif choice == "2":
            table_name = input("表示したいテーブル名を入力してください: ")

            # TODO: 入力された table_name のデータを pandas で読み込む
            # ヒント:
            # query = f"SELECT ...."

            while True:
                print("\n--- 保存メニュー ---")
                print("1. CSVとして保存する")
                print("2. JSONとして保存する")
                print("3. 前のメニューに戻る")

                save_choice = input("番号を選んでください: ")

                if save_choice == "1":
                    # TODO: df を CSV として保存する
                    # ファイル名は table_name + ".csv" にする
                    # index=False, encoding="utf-8-sig" を指定する
                    pass
                elif save_choice == "2":
                    # TODO: df を JSON として保存する
                    # ファイル名は table_name + ".json" にする
                    # orient="records", force_ascii=False, indent=2 を指定する
                    pass
                elif save_choice == "3":
                    break
                else:
                    print("その番号はありません")
        elif choice == "0":
            break
        else:
            print("その番号はありません")
