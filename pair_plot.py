import pandas as pd
from tools import *
import sys
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    test = pd.read_csv(sys.argv[1])
    i = 0
    for features in test.columns:
        if i > 18 or i == 0 or features == "Arithmancy" or features == "Potions" or features == "Care of Magical Creatures":
            del test[features]
        i += 1
    print(test)
    sns.pairplot(test, hue='Hogwarts House', height=1.5)
    plt.show()