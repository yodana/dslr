from math import nan
import numpy as np
import pandas as pd
import sys
from sklearn import preprocessing
from sklearn import impute

if __name__ == '__main__':
    test = pd.read_csv(sys.argv[1])
    matrice = np.loadtxt("theta.txt")
    i = 0
    real_houses = test["Hogwarts House"]
    for features in test.columns:
        n = test[features].size
        if i < 6 or features == "Arithmancy" or features == "Potions" or features == "Care of Magical Creatures":
            del test[features]
        i += 1
    i = 0
    theta = np.array(matrice)
    houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
    c = np.ones((576))
    i = 0
    for features in test.columns:
        a = np.array((test[features]))
        c = np.concatenate((a,c))
        i += 1
    c = np.reshape(c, (i + 1, n)).T
    imputer = impute.SimpleImputer(missing_values=nan,strategy="mean")
    c = imputer.fit_transform(c)
    i = 0
    for column in c.T:
        if (matrice[:,1][i] != 0):
            c[:,i] = (column - matrice[:,0][i]) / matrice[:,1][i]
        i += 1
    c[:,-1] = np.ones((576))
    j = 0
    resultat = 0
    i = 0
    theta = np.delete(theta, 0, 1)
    theta = np.delete(theta, 0, 1)
    print(theta)
    for student in c:
        maximum = [0, 0, 0, 0]
        for i in range(0, 4):
            maximum[i] = float(1/(1 + np.exp(np.negative(np.dot(student, theta[:,i])))))
        if houses[maximum.index(max(maximum))] == real_houses[j]:
            resultat += 1
        print(maximum)
        j += 1
        print(houses[maximum.index(max(maximum))])
    print("Un resultat de:", 100*(resultat/(j)))
    print(resultat)