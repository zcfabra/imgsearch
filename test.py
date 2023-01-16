#!/usr/bin/python3

import torch
import numpy as np
from PIL import Image
import os, sys
import cv2
from simsearch import simsearch
import torchvision
device = torch.device("mps")
def main():

	args = sys.argv
	if len(args) <2:
		print("[X] MUST SPECIFCY AN IMAGE")
		sys.exit(0)

	x = torch.tensor(cv2.imread(args[1]))
	x = x.unsqueeze(0).permute(0,3,1,2).float() / 255
	x= x.to(device)
	assert x.shape[:2] == (1,3)
	print(x.dtype, x.min(),x.max())
	model = simsearch.get_efficientnet_chopped().to(device)
	model.eval()
	o = model(x)


if __name__ == "__main__":
	main()

