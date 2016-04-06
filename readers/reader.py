import pandas as pd
import zipfile


class DataReader():
    def __init__(self):
        self.drive = '../input/'
        self.z = zipfile.ZipFile(self.drive+'train.csv.zip')
        self.train = pd.read_csv(self.z.open('train.csv'))
        self.cats = list(set(self.train.Category))

    def get_column_names(self):
        names = []
        for name in self.train:
            names.append(name)

    def get_categories(self):
        return self.cats

    def get_raws(self):
        '''
        Returns a generator for raw information: Dates, Category, Descript DayOfWeek,
        PdDistrict, Resolution Address X Y
        '''
        for i in range(self.get_length()):
            raw = self.get_raw(i)
            yield raw

    def get_length(self):
        return len(self.train.Category)

    def get_raw(self, num):
        '''
        Get raw by line number
        '''
        raw={}
        if num<0 or num>self.get_length():
            return raw
        raw['date'] = self.train.Dates[num]
        raw["category"] = self.train.Category[num]
        raw["description"] = self.train.Descript[num]
        raw["day"] = self.train.DayOfWeek[num]
        raw["pddistrict"] = self.train.PdDistrict[num]
        raw["resolution"] = self.train.Resolution[num]
        raw["address"] = self.train.Address[num]
        raw["x"] = self.train.X[num]
        raw["y"] = self.train.Y[num]
        return raw
