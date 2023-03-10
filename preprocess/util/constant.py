import os
import logging
import torch

ROOT_PATH = "/home/u190110105/insCar"
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# device = torch.device("mps")
# device = torch.device("cpu")

logger = logging.getLogger(__file__)
logging.basicConfig(
    format="[%(asctime)s - %(filename)s:line %(lineno)s] %(message)s",
    datefmt='%d %b %H:%M:%S',
    level=logging.INFO)
# logger.setLevel(logging.INFO)
