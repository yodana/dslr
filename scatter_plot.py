import pandas as pd
import sys
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pd.read_csv(sys.argv[1])
    plt.scatter(data['Defense Against the Dark Arts'], data['Astronomy'])
    plt.xlabel("Defense Against the Dark Arts")
    plt.ylabel("'Astronomy")
    plt.show()