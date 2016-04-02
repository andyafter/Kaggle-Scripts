import pandas as pd
import zipfile

drive = './'
z = zipfile.ZipFile(drive+'train.csv.zip')
train = pd.read_csv(z.open('train.csv'))
cats = list(set(train.Category))
print cats
