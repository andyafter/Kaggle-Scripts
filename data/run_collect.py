from cexio import TickerData
import json


t = TickerData()


items = []
items.append("timestamp")
items.append("pair")
items.append("low")
items.append("high")
items.append("last")
items.append("volume")
items.append("volume30d")
items.append("bid")
items.append("ask")
head = "\t".join(items)+'\n'


data = json.loads(t.tick())["data"]
for fnum in range(10):
    fname = "tick_data"+str(fnum)+".txt"
    f = open(fname, 'w')
    f.write(head)
    for i in range(100000):
        data = json.loads(t.tick())["data"]
        for j in range(len(data)):
            row = "\t".join([str(data[j][item]) for item in items])
            row += '\n'
            f.write(row)
            print row
    f.close()
