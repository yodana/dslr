import pandas as pd
from tools import *
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class Matrice(object):
    def __init__(self, data):
        self.X = self.get_X(data)
        self.Y = self.get_Y(data)
        self.theta = self.get_theta(0, 0, 0)

    def get_X(self, data):
        ret = []
        ret1 = []
        for notes in data["Herbology"]:
            ret.append(notes)
        test = np.array(ret).reshape(27, 1)
        print(test)
        for notes in data["History of Magic"]:
            ret1.append(notes)
            ret1.append(1)
        m = np.array(ret1).reshape(27, 2)
        test = np.concatenate((test, m), axis=1)
        return test
    
    def get_Y(self, data):
        ret = []
        for house in data["Hogwarts House"]:
            if house == "Gryffindor":
                ret.append(1)
            else:
                ret.append(0)
        M = np.array(ret).reshape(27, 1)
        return M
    
    def get_theta(self, t1, t2, t3):
        M = np.array([t1, t2, t3])
        M = M.reshape(3, 1)
        return M

if __name__ == '__main__':
    test = pd.read_csv(sys.argv[1])
    i = 0
    for features in test.columns:
        if features != "History of Magic" and features != "Herbology" and features != "Hogwarts House":
            del test[features]
        i += 1
    #sns.pairplot(test, hue='Hogwarts House', height=1.5)
    matrice = Matrice(test)
    plt.show()