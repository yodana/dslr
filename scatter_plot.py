import pandas as pd
from tools import *
import sys
import matplotlib.pyplot as plt

if __name__ == '__main__':
    test = pd.read_csv(sys.argv[1])
    plt.scatter(test['Herbology'], test['Astronomy'])
    plt.show()