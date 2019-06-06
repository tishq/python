import math


def UserSimilarity(train):
    W = dict()
    for u in train.keys():
        for v in train.keys():
            if u == v:
                continue
        W[u][v] = len(train[u] & train[v])
        W[u][v] /= math.sqrt(len(train[u]) * len(train[v]) * 1.0)
    return W
if __name__ == '__main__':
    train = {'A': {'a','b','c'},'B': {'a','b','c','d'}}
    aa = UserSimilarity(train)
    print(aa)