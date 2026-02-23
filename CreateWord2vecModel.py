import glob
from gensim.models import Word2Vec
import json
import gc
from gensim.models import Phrases

datas = []
for filname in glob.glob('QuantitativeBias/*'):
    print(filname)
    with open(filname) as f:
        data = json.load(f)
        for i in data:
            datas.extend(i)
        del data
        gc.collect()

bigram_transformer = Phrases(datas)
bigram_transformer.save("ind_bigram")

# bigram_transformer = Phrases.load("ind_bigram/gram_model.pkl")
model = Word2Vec(bigram_transformer[datas], vector_size=100, window=10, min_count=3, workers=64, sg=1, hs=0, negative=10, epochs=10)
model.save('FMOGB/ind.model')

