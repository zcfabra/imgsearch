#!/usr/bin/python3

import torch
import numpy as np
from PIL import Image
import os, sys
import cv2
from simsearch import simsearch, utils
import torchvision
device = torch.device("mps")
import sqlite3 as sql
import io


def main():

	# args = sys.argv
	# if len(args) <2:
	# 	print("[X] MUST SPECIFCY AN IMAGE")
	# 	sys.exit(0)

	# db = sql.connect("temp.sqlite", detect_types=sql.PARSE_DECLTYPES)
	# c = db.cursor()
	# sql.register_adapter(np.ndarray, utils.arr_to_text)
	# sql.register_converter("array", utils.text_to_arr)
	# c.execute(''' SELECT count(name) from sqlite_master WHERE type='table' AND name= 'test' ''')
	# if (c.fetchone()[0] ==1):
	# 	print("TABLE exists")
	# else:
	# 	print("TABLE DOES NOT EXIST")
	# 	c.execute("CREATE table test (name VARCHAR(255) PRIMARY KEY ,arr array)")

	# simsearch.add_dir_to_db(args[1], c)
	# db.commit()
	model = simsearch.get_efficientnet_chopped()
	
	


if __name__ == "__main__":
	main()

