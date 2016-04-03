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
        self.drive = '../input/'
        self.z = zipfile.ZipFile(self.drive+'train.csv.zip')
        self.train = pd.read_csv(self.z.open('train.csv'))
        self.cats = list(set(self.train.Category))

    def read(self):
        pass

    def get_column_names(self):

        pass

    def get_categories(self):
        return self.cats
