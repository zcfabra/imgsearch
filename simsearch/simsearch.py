import torch
import torch.nn as nn
import numpy as np
import torchvision.models

def get_dims(inp: np.array):
    print(f"DIMENSIONS OF IMAGE: {inp.shape}")

def get_efficientnet_chopped():
    base=  torchvision.models.efficientnet_v2_l()
    return nn.Sequential(*list(base.children())[:-1])
