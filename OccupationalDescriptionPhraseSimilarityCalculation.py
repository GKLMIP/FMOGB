import gensim
from gensim import models
from gensim.models import word2vec
from gensim.similarities import WmdSimilarity
from gensim.models import KeyedVectors
import pandas
import math
from gensim.models import Phrases

# 将 Word2Vec 转换成 KeyedVectors
# model = models.Word2Vec.load('ind/ind.model')
# vectors = model.wv
# vectors.save("vectors_wv")


bigram_reloaded = Phrases.load("part50/gram_model.pkl")
model = models.Word2Vec.load('part50/ind.model')
word_vectors = model.wv
words = pandas.read_excel('Occupations.xlsx').values.tolist()
for word in words:
    # print(word)
    try:
        math.isnan(word[2])
        words = word[1].split(',')
        sim_average = 0
        for word_ in words:
            word_1 = word_.strip() + ' laki-laki'
            word_2 = word_.strip() + ' perempuan'
            word_3 = word_.strip() + ' wanita'
            try:
                word_1_top100 = [_[0] for _ in word_vectors.most_similar(bigram_reloaded[word_1.split()], topn=100)]
            except:
                word_1_top100 = []
            try:
                word_2_top100 = [_[0] for _ in word_vectors.most_similar(bigram_reloaded[word_2.split()], topn=100)]
            except:
                word_2_top100 = []
            try:
                word_3_top100 = [_[0] for _ in word_vectors.most_similar(bigram_reloaded[word_3.split()], topn=100)]
            except:
                word_3_top100 = []

            # print(word_1_top100)
            # print(word_2_top100)
            # print(word_3_top100)
            try:
                sim1 = len(list(set(word_1_top100).intersection(set(word_2_top100)))) / len(list(set(word_1_top100).union(set(word_2_top100))))
            except:
                sim1 = 0
            try:
                sim2 = len(list(set(word_1_top100).intersection(set(word_3_top100)))) / len(list(set(word_1_top100).union(set(word_3_top100))))
            except:
                sim2 = 0
            # print(len(list(set(word_1_top100).intersection(set(word_2_top100)))))
            sim = (sim1 + sim2) / 2
            sim_average += sim
        sim_average = sim_average / len(words)
        print(word[0], '\t', sim_average)
    except:
        word1 = word[2]
        words2 = word[3].split(',')
        sim_average = 0
        for word2 in words2:
            word2 = word2.strip()
            word_1_top100 = [_[0] for _ in word_vectors.most_similar(bigram_reloaded[word1.split()], topn=100)]
            try:
                word_2_top100 = [_[0] for _ in word_vectors.most_similar(bigram_reloaded[word2.split()], topn=100)]
            except:
                word_2_top100 = []
                print(1)
            sim = len(list(set(word_1_top100).intersection(set(word_2_top100)))) / len(list(set(word_1_top100).union(set(word_2_top100))))
            sim_average += sim
        sim_average = sim_average / len(words2)
        print(word[0], '\t', sim_average)
