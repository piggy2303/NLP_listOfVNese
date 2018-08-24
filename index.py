import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None


def select_all_tasks(conn, tableName):
    cur = conn.cursor()
    string = "SELECT MEANING FROM " + tableName
    print(string)
    cur.execute(string)
    rows = cur.fetchall()
    temp = ''
    for row in rows:
        temp = temp + str(row) + "\n"
    return temp


def main():
    database = "./VietEngDicDB.db"
    conn = create_connection(database)

    arrTable = [
        "za",
        "zb",
        "zc",
        "zd",
        "ze",
        "zg",
        "zh",
        "zi",
        "zk",
        "zl",
        "zm",
        "zn",
        "zo",
        "zp",
        "zq",
        "zr",
        "zs",
        "zt",
        "zu",
        "zv",
        "zx",
        "zy",
        "zà",
        "zá",
        "zâ",
        "zè",
        "zé",
        "zê",
        "zì",
        "zí",
        "zò",
        "zó",
        "zô",
        "zõ",
        "zù",
        "zú",
        "zý",
        "ză",
        "zđ",
        "zơ",
        "zư",
        "zạ",
        "zả",
        "zấ",
        "zầ",
        "zẩ",
        "zậ",
        "zắ",
        "zẳ",
        "zẵ",
        "zẹ",
        "zẻ",
        "zẽ",
        "zế",
        "zề",
        "zễ",
        "zệ",
        "zỉ",
        "zị",
        "zọ",
        "zỏ",
        "zố",
        "zồ",
        "zổ",
        "zộ",
        "zớ",
        "zờ",
        "zở",
        "zỡ",
        "zợ",
        "zụ",
        "zủ",
        "zứ",
        "zử",
        "zự",
        "zỷ",
    ]

    with conn:
        print("2. Query all tasks")
        with open("input.txt", "wt") as fout:
            for item in arrTable:
                fout.write(select_all_tasks(conn, item))

if __name__ == '__main__':
    main()
