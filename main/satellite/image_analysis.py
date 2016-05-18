import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import glob, os

from subprocess import check_output


smjpegs = [f for f in glob.glob("../../input/satellite/train_sm/*.jpeg")]
set175 = [smj for smj in smjpegs if "set175" in smj]

# basic exploration

first = plt.imread('../../input/satellite/train_sm/set175_1.jpeg')
dims = np.shape(first)

pixel_matrix = np.reshape(first, (dims[0] * dims[1], dims[2]))
#plt.scatter(pixel_matrix[:,0], pixel_matrix[:,1])
_ = plt.hist2d(pixel_matrix[:,1], pixel_matrix[:,2], bins=(50,50))

