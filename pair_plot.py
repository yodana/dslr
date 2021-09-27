import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    file = pd.read_csv(sys.argv[1])
    i = 0
    for features in file.columns:
        if i != 1 and (i < 6 or features == "Arithmancy" or features == "Potions" or features == "Care of Magical Creatures"):
            del file[features]
        i += 1
    sns.pairplot(file, hue='Hogwarts House', height=1.5)
    plt.show()