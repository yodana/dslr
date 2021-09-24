import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    file = pd.read_csv(sys.argv[1])
    i = 0
    for features in file.columns:
        if i > 18 or i == 0:
            del file[features]
        i += 1
    sns.pairplot(file, hue='Hogwarts House', height=1.5)
    plt.show()