import pandas as pd
from tools import *
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from Encoder import *
from sklearn import preprocessing
from sklearn import impute
from Math import *

class Matrice(object):
    def __init__(self, data, data_y):
        self.min_max_scaler = preprocessing.Normalizer()
        self.size_lines = np.size(data, 0)
        self.size_columns = np.size(data, 1)
        self.resultat = np.zeros(shape=(self.size_columns, 6))
        self.X = self.get_X(data)
        self.theta = self.get_theta(self.size_columns)
        self.get_resultat(data_y)
    
    def get_resultat(self, data_y):
        houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
        for i in range(0, 4):
            self.theta = self.get_theta(self.size_columns)
            self.Y = self.get_Y(data_y, houses[i])
            self.gradient_descent(i)
        np.savetxt("theta.txt", self.resultat)

    def get_X(self, data):
        i = 0
        mean = []
        std = []
        imputer = impute.SimpleImputer(missing_values=nan,strategy="mean")
        X = imputer.fit_transform(data)
        print(X)
        for column in X.T:
            math = Math(column)
            X[:,i] = (column - math.mean) / math.std
            i += 1
            mean.append(math.mean)
            std.append(math.std)
        self.resultat[:,0] = np.array(mean) 
        self.resultat[:,1] = np.array(std)
        #X = self.min_max_scaler.fit_transform(X)
        X[:,-1] = np.ones((self.size_lines))
        print(X)
        return X
    
    def get_Y(self, data, present_house):
        ret = []
        for house in data:
            if house == present_house:
                ret.append(1)
            else:
                ret.append(0)
        M = np.array(ret).reshape(self.size_lines, 1)
        return M
    
    def get_theta(self, size):
        M = np.zeros((size, 1))
        return M

    def model(self):
        return 1/(1 + np.exp(np.negative(np.dot(self.X, self.theta))))

    def gradient(self):
        return 1/self.size_lines * self.X.T.dot(self.model() - self.Y)

    def gradient_descent(self, k):
        for i in range(1, 1000):
            self.theta = self.theta - 0.9 * self.gradient()
        self.resultat[:,k+2] = self.theta[:,0]
        plt.plot(self.X, self.model())
        #plt.show()

if __name__ == '__main__':
    test = pd.read_csv(sys.argv[1])
    i = 0
    houses = test["Hogwarts House"]
    for features in test.columns:
        n = test[features].size
        if i < 6 or features == "Arithmancy" or features == "Potions" or features == "Care of Magical Creatures":
            del test[features]
        i += 1
    m = 0
    n = test[features].size
    c = np.ones((n))
    imputer = impute.SimpleImputer(missing_values=nan,strategy="mean")
    for features in test.columns:
        a = np.array(test[features])
        c = np.concatenate((a,c))
        m += 1
    c = np.reshape(c, (m + 1, n)).T
    matrice = Matrice(c, houses)
