import sqlite3
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "Stypress-Courses" / "012-Database-Python" / "retn5_dat.txt"
DB = Path(__file__).with_name("retention.db")


def parse(line):
    # fields are separated by ^, text fields are wrapped in ~
    return [field.strip("~") for field in line.rstrip("\r\n").split("^")]


assert parse("~1951~^~VEAL, BROILED~^~301~^~Calcium, Ca~^~95~^~~^~~\r\n")[:5] == \
    ["1951", "VEAL, BROILED", "301", "Calcium, Ca", "95"]


def load(connection, path):
    connection.executescript("""
        DROP TABLE IF EXISTS retention;
        CREATE TABLE retention (
            retn_code TEXT,
            description TEXT,
            nutr_no TEXT,
            nutr_desc TEXT,
            retn_factor INTEGER,
            PRIMARY KEY (retn_code, nutr_no)
        );
    """)
    with open(path, encoding="ascii") as file:
        rows = [parse(line)[:5] for line in file if line.strip()]
    connection.executemany("INSERT INTO retention VALUES (?, ?, ?, ?, ?)", rows)
    connection.commit()
    return len(rows)


if __name__ == "__main__":
    with sqlite3.connect(DB) as connection:
        print("Loaded rows:", load(connection, DATA))
        for (description,) in connection.execute(
                "SELECT DISTINCT description FROM retention WHERE description LIKE '%VEAL%' ORDER BY description"):
            print(description)
