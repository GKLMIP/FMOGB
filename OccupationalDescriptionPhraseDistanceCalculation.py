import gensim
from gensim import models
from gensim.models import word2vec
from gensim.similarities import WmdSimilarity
from gensim.models import KeyedVectors
import pandas
import math
from gensim.models import Phrases


# WMD 2-gram
bigram_reloaded = Phrases.load("part90/gram_model.pkl")
model = models.Word2Vec.load('part90/ind.model')
word_vectors = model.wv
# word_vectors = KeyedVectors.load("vectors_wv", mmap='r')
words = pandas.read_excel('Occupations.xlsx').values.tolist()
for word in words:
    # print(word)
    try:
        math.isnan(word[2])
        words = word[1].split(',')
        distance_average = 0
        for word_ in words:
            word_1 = word_.strip() + ' laki-laki'
            word_2 = word_.strip() + 'perempuan'
            word_3 = word_.strip() + ' wanita'
            distance1 = word_vectors.wmdistance(word_1, word_2)
            distance2 = word_vectors.wmdistance(word_1, word_3)
            # distance1 = word_vectors.n_similarity(bigram_reloaded[word_1.split(' ')], bigram_reloaded[word_2.split(' ')])
            # distance2 = word_vectors.n_similarity(bigram_reloaded[word_1.split(' ')], bigram_reloaded[word_3.split(' ')])
            distance = (distance2 + distance1) / 2
            distance_average += distance
        distance_average = distance_average / len(words)
        print(word[0], '\t', distance_average)
    except:
        word1 = word[2]
        words2 = word[3].split(',')
        distance_average = 0
        for word2 in words2:
            word2 = word2.strip()
            distance_average += word_vectors.wmdistance(word1, word2)
            # distance_average += word_vectors.n_similarity(bigram_reloaded[word1.split(' ')], bigram_reloaded[word2.split(' ')])
        distance_average = distance_average / len(words2)
        print(word[0], '\t', distance_average)

