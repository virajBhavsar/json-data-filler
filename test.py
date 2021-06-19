from refine import Merger
import json

m = Merger()
datafile = m.getFiles('schema.json','data.json')
data = m.refine(datafile[0],datafile[1])

y = json.dumps(data)
with open('output.json','w') as f:
    f.write(y)

f.close()
