#!/usr/bin/python3
import sqlite3 as sql
import numpy as np
from simsearch import utils
def main():
    db = sql.connect("temp.sqlite", detect_types=sql.PARSE_DECLTYPES)
    c = db.cursor()
    sql.register_adapter(np.ndarray, utils.arr_to_text)
    sql.register_converter("array", utils.text_to_arr)
    c.execute("SELECT arr FROM test")
    data = c.fetchone()[0]
    print(data.shape)



if __name__ == "__main__":
    main()