import json
import sqlite3
import subprocess
import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def run_task(task_name, user_input, timeout=10):
    task_dir = ROOT / task_name
    script = task_dir / f"{task_name}.py"

    result = subprocess.run(
        [sys.executable, script.name],
        input=user_input,
        text=True,
        capture_output=True,
        cwd=task_dir,
        timeout=timeout,
    )

    assert result.returncode == 0, (
        f"{script} が正常に終了しませんでした。\n"
        f"stdout:\n{result.stdout}\n"
        f"stderr:\n{result.stderr}"
    )
    return result.stdout


def remove_if_exists(path):
    if path.exists():
        path.unlink()


def test_task01_view_students_data():
    output = run_task("task01", "1\n3\n2\n2\n4\n0\n")

    assert "佐藤葵" in output
    assert "高橋凛" in output
    assert "金子陽" in output
    assert "和田美羽" in output
    assert "50" in output and "9" in output


def test_task02_tourist_analysis():
    task_dir = ROOT / "task02"
    df = pd.read_csv(task_dir / "tourists.csv")

    output = run_task("task02", "1\n2\n3\n4\n5\n6\n300000\n7\n0\n")

    assert str(df["年齢"].mean()) in output
    assert df["国"].value_counts().idxmax() in output
    assert str(df["使用金額"].max()) in output
    assert df.loc[df["使用金額"].idxmax(), "名前"] in output
    assert str(df["滞在日数"].mean()) in output
    assert "Joshua Murphy" in output
    assert "Emma Smith" in output


def test_task03_filter_hotel_guests():
    output = run_task("task03", "4\nアメリカ\n6\n0\n")

    assert "Daniel Allen" in output
    assert "Andrew Reed" in output
    assert "Nathan Rivera" in output
    assert "Emma Smith" not in output


def test_task04_sort_products():
    output = run_task("task04", "1\n4\n3\n0\n")

    assert "USBメモリ A" in output
    assert "USBメモリ B" in output
    assert output.index("USBメモリ A") < output.index("USBメモリ B")
    assert "グラフィックボード B" in output
    assert "外付けSSD B" in output
    assert "プロジェクター B" in output


def test_task05_order_aggregation():
    task_dir = ROOT / "task05"
    df = pd.read_csv(task_dir / "orders.csv")

    output = run_task("task05", "1\n2\n3\n4\n5\n6\n7\n0\n")

    assert str(len(df)) in output
    assert str(df["合計金額"].sum()) in output
    assert str(df["合計金額"].mean()) in output
    assert df["支払方法"].value_counts().idxmax() in output
    assert "食品" in output
    assert "東京" in output
    assert str(df["合計金額"].max()) in output


def test_task06_groupby_school_scores():
    output = run_task("task06", "1\n2\n3\n4\n5\n6\n0\n")

    assert "IT" in output
    assert "デザイン" in output
    assert "ビジネス" in output
    assert "医療" in output
    assert "本校" in output
    assert "分校" in output
    assert "田中" in output


def test_task07_save_salary_result_csv():
    task_dir = ROOT / "task07"
    result_csv = task_dir / "result.csv"
    remove_if_exists(result_csv)

    run_task("task07", "1\n2\n3\n5\n0\n")

    assert result_csv.exists(), "result.csv が作成されていません。"
    result_df = pd.read_csv(result_csv)

    assert "残業代" in result_df.columns
    assert "総支給額" in result_df.columns
    assert "評価結果" in result_df.columns
    assert result_df.loc[0, "残業代"] == 21600
    assert result_df.loc[0, "総支給額"] == 351600
    assert result_df.loc[0, "評価結果"] == "普通"
    assert result_df.loc[1, "評価結果"] == "優秀"


def test_task08_combine_players_and_write_report():
    task_dir = ROOT / "task08"
    result_csv = task_dir / "players_result.csv"
    result_txt = task_dir / "result.txt"
    remove_if_exists(result_csv)
    remove_if_exists(result_txt)

    run_task("task08", "2\n3\n4\n0\n")

    assert result_csv.exists(), "players_result.csv が作成されていません。"
    assert result_txt.exists(), "result.txt が作成されていません。"

    result_df = pd.read_csv(result_csv)
    assert len(result_df) == 20
    assert "最大レベルとの差" in result_df.columns
    assert int(result_df.loc[result_df["名前"] == "Daichi", "最大レベルとの差"].iloc[0]) == 0
    assert int(result_df.loc[result_df["名前"] == "Aoi", "最大レベルとの差"].iloc[0]) == 28

    text = result_txt.read_text(encoding="utf-8")
    assert "20" in text
    assert "187.55" in text or "187.5" in text
    assert "4" in text
    assert "戦士" in text and "109100" in text
    assert "魔法使い" in text and "104700" in text


def test_task09_read_sql_and_export():
    task_dir = ROOT / "task09"
    students_csv = task_dir / "students.csv"
    scores_json = task_dir / "scores.json"
    remove_if_exists(students_csv)
    remove_if_exists(scores_json)

    output = run_task("task09", "1\n2\nstudents\n1\n3\n2\nscores\n2\n3\n0\n")

    assert "students" in output
    assert "courses" in output
    assert "scores" in output
    assert "departments" in output
    assert students_csv.exists(), "students.csv が作成されていません。"
    assert scores_json.exists(), "scores.json が作成されていません。"

    students = pd.read_csv(students_csv)
    assert len(students) == 12
    assert "田中" in students.to_string()

    with scores_json.open(encoding="utf-8") as file:
        scores = json.load(file)
    assert isinstance(scores, list)
    assert len(scores) == 12
    assert any(row.get("course_name") == "Python基礎" for row in scores)


def test_task10_clean_dirty_sales_csv():
    task_dir = ROOT / "task10"
    cleaned_csv = task_dir / "cleaned_sales.csv"
    remove_if_exists(cleaned_csv)

    run_task("task10", "4\n5\n6\n7\n8\n0\n")

    assert cleaned_csv.exists(), "cleaned_sales.csv が作成されていません。"
    df = pd.read_csv(cleaned_csv)

    assert "メモ" not in df.columns
    assert "order_id" in df.columns
    assert "product_name" in df.columns
    assert "quantity" in df.columns
    assert "unit_price" in df.columns
    assert "discount" in df.columns

    total_column = "total_amount" if "total_amount" in df.columns else "合計金額"
    assert total_column in df.columns
    assert df.loc[0, total_column] == 93000
