import io
import numpy as np
import sqlite3 as sql

def arr_to_text(arr: np.array):
	out = io.BytesIO()
	np.save(out, arr)
	out.seek(0)
	return sql.Binary(out.read())


def text_to_arr(text):
	out = io.BytesIO(text)
	out.seek(0)
	return np.load(out, allow_pickle=True)
