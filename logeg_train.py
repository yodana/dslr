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
        print(self.X)
        self.gradient_descent()

    def get_X(self, data):
        ret = []
        ret1 = []
        for notes in data["Divination"]:
            ret.append(notes)
        test = np.array(ret).reshape(23, 1)
        for notes in data["Defense Against the Dark Arts"]:
            ret1.append(notes)
            ret1.append(1)
        m = np.array(ret1).reshape(23, 2)
        test = np.concatenate((test, m), axis=1)
        return test
    
    def get_Y(self, data):
        ret = []
        for house in data["Hogwarts House"]:
            if house == "Gryffindor":
                ret.append(1)
            else:
                ret.append(0)
        M = np.array(ret).reshape(23, 1)
        return M
    
    def get_theta(self, t1, t2, t3):
        M = np.array([t1, t2, t3])
        M = M.reshape(3, 1)
        return M

    def model(self):
        #return np.dot(self.X, self.theta)
        return 1/(1 + np.exp(np.negative(np.dot(self.X, self.theta))))

    def gradient(self):
        return 1/23 * self.X.T.dot(self.model() - self.Y)

    def gradient_descent(self):
        for i in range(1, 100):
            self.theta = self.theta - 0.5 * self.gradient()
        print("theta final:", self.theta)
        plt.plot(self.X, self.model())
        plt.show()

if __name__ == '__main__':
    test = pd.read_csv(sys.argv[1])
    i = 0
    for features in test.columns:
        if features != "Divination" and features != "Defense Against the Dark Arts" and features != "Hogwarts House":
            del test[features]
        i += 1
    sns.pairplot(test, hue='Hogwarts House', height=1.5)
    matrice = Matrice(test)
