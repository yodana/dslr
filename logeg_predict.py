import numpy as np
import pandas as pd
import sys

if __name__ == '__main__':
    test = pd.read_csv(sys.argv[1])
    for features in test.columns:
        if features != "Divination" and features != "Defense Against the Dark Arts" and features != "Hogwarts House":
            del test[features]
    theta = np.array([[1.41139367], [-1.3424048], [0.01091449]])
    print(theta)
    print(test["Divination"][0])
    X = np.array([test["Divination"][0], test["Defense Against the Dark Arts"][0], 1])
    print(X)
    print(float(1/(1 + np.exp(np.negative(np.dot(X, theta))))))

