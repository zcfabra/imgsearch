
import os
import torch
import torch.nn as nn
import numpy as np
import torchvision.models
import cv2
from sqlite3 import Cursor
device = torch.device("mps")



def get_dims(inp: np.array):
    print(f"DIMENSIONS OF IMAGE: {inp.shape}")

def get_efficientnet_chopped():
    base = torchvision.models.efficientnet_v2_l(
        torchvision.models.EfficientNet_V2_L_Weights)
    return nn.Sequential(*list(base.children())[:-1])

def add_dir_to_db(dirname: str, c):
    x = os.listdir(dirname)
    for each in x:
        print(each)
        path = os.path.join(dirname, each)
        print(os.path.isfile(path))
        if os.path.isfile(path):
            add_file_embedding_to_db(path, c)


def add_file_embedding_to_db(file_path: str, c: Cursor):
    """DOES NOT COMMIT TO DB"""
    x = torch.tensor(cv2.imread(file_path))
    x = x.unsqueeze(0).permute(0, 3, 1, 2).float() / 255
    x= x.to(device)
    assert x.shape[:2] == (1,3)
    print(x.dtype, x.min(),x.max())
    with torch.no_grad():
        model = get_efficientnet_chopped().to(device)
        model.eval()
        o = model(x)
        print(o.shape)
        o_np = o.cpu().detach().numpy()

        c.execute("INSERT INTO test (name , arr) values (?,?)", (file_path, o_np))










def get_cosine_similarity(a:np.array, b:np.array):
    return (np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))).item()