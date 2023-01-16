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

	args = sys.argv
	if len(args) <2:
		print("[X] MUST SPECIFCY AN IMAGE")
		sys.exit(0)

	db = sql.connect("temp.sqlite", detect_types=sql.PARSE_DECLTYPES)
	c = db.cursor()
	c.execute(''' SELECT count(name) from sqlite_master WHERE type='table' AND name= 'test' ''')
	if (c.fetchone()[0] ==1):
		print("TABLE exists")
	else:
		print("TABLE DOES NOT EXIST")
		sql.register_adapter(np.ndarray, utils.arr_to_text)
		sql.register_converter("array", utils.text_to_arr)
		c.execute("CREATE table test (arr array)")

	x = torch.tensor(cv2.imread(args[1]))
	x = x.unsqueeze(0).permute(0,3,1,2).float() / 255
	x= x.to(device)
	assert x.shape[:2] == (1,3)
	print(x.dtype, x.min(),x.max())
	with torch.no_grad():
		model = simsearch.get_efficientnet_chopped().to(device)
		model.eval()
		o = model(x)
		print(o.shape)
		o_np = o.cpu().detach().numpy()

		c.execute("INSERT INTO test (arr) values (?)", (o_np, ))
		db.commit()


	


if __name__ == "__main__":
	main()

