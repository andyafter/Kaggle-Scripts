Readers

# Reading Datasets
Reader classes provide reusable classes to read datasets for Kaggle competitions.

# Examples
- An example of getting a generator of raws of train.csv
```python
from readers.reader import DataReader

dr = DataReader()
dr.get_raws()
for raw in dr:
    print raw["date"]
```
