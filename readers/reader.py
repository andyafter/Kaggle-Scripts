import os
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from time import time
import seaborn as sns
import pandas as pd
import scipy
import zipfile
from matplotlib.backends.backend_pdf import PdfPages


class DataReader():
    def __init__(self):
        pass
    def read(self):
        drive = '../input/'
        z = zipfile.ZipFile(drive+'train.csv.zip')
        train = pd.read_csv(z.open('train.csv'))
        print "success"
