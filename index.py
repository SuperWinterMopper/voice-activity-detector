from __future__ import annotations
import os
import math
import argparse
from dataclasses import dataclass
from typing import List, Tuple, Dict


import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torchaudio
from torchaudio.transforms import MelSpectrogram, AmplitudeToDB, TimeMasking, FrequencyMasking


def main():
    x = 1
    pass

if __name__ == '__main__':
    main()