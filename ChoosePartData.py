import glob
from gensim.models import Word2Vec
import json
import gc
from gensim.models import Phrases

part_datas = []
for filname in glob.glob('QuantitativeBias/*.json'):
    print(filname)
    with open(filname) as f:
        datas = json.load(f)
        for num, data in enumerate(datas):
            if num % 10 < 4:
                part_datas.append(datas[data])

with open('part40.json','w') as f:
    json.dump(part_datas,f)