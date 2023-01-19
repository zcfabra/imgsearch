#!/usr/bin/python3
import sqlite3 as sql
import numpy as np
from simsearch import utils
def main():
    db = sql.connect("temp.sqlite", detect_types=sql.PARSE_DECLTYPES)
    c = db.cursor()
    sql.register_adapter(np.ndarray, utils.arr_to_text)
    sql.register_converter("array", utils.text_to_arr)
    c.execute("SELECT * FROM test")
    data = c.fetchall()
    N_HYPERPLANES=4
    hyperplanes = np.random.randn(1280,N_HYPERPLANES)
    
    for row in data:
        tens = row[1].squeeze(0).squeeze(1).squeeze(1)
        # print(tens.shape)
        out = np.dot(tens, hyperplanes)
        out[out > 0] = 1
        out[out <=0] = 0
        print(row[0],out)



if __name__ == "__main__":
    main()