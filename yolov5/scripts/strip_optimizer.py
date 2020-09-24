import sys
import torch
sys.path.insert(0, './')
from utils.general import strip_optimizer


strip_optimizer(sys.argv[1])
