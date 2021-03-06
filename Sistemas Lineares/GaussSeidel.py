#gauss suicidal

import numpy as np
from scipy.linalg import solve
import collections

def gauss(A, b, x):
    L = np.tril(A)
    U = A - L
    x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
    print(x)
    return x            

def gausssidel(A,b,tol,lim):
    cont = 0
    x = [1, 1, 1]
    while(True):
        old = x
        x = gauss(A,b,x)
        cont = cont + 1
        tols = []
        for val1,val2 in zip(x,old):
            if((abs(val1-val2))<tol):
                tols.append(True)
            else:
                tols.append(False)
        aux = np.all(tols)
        if np.allclose(x,old) or aux or cont == lim:
            return x

A = np.array([[1.0, 0.0, -1.0], [-0.5, 1.0, -0.25], [1.0, -0.5, 1.0]])
b = [0.2, -1.425, 2.0]

val = gausssidel(A,b,1e-2,300)
print(val)