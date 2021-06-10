from numpy import NaN
import pandas as pd
from tools import *
import sys

def describe(data, feature, i):
    if i < 6:
        return -1
    describe = {
        'Count': 0,
        'Mean':0,
    }
    for d in data:
        describe['Count'] += 1
        if d.isnull().values.any(): # finir describe et voir cmt check si une valeur est nan in pandas
            print(d)
    return describe
    #for d in data:
     #   print(d)

if __name__ == '__main__':
    test = pd.read_csv(sys.argv[1])
    count = 0
    i = 0
    data_describe = {}
    for features in test.columns:
        description = describe(test[features], features, i)
        i = i + 1
        if description != -1:
            data_describe[features] = description
    print(pd.DataFrame(data_describe))
