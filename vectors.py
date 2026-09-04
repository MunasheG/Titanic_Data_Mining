import numpy as np
import math as m

def rescale(a):
    n_row = a.shape[0]
    n_col = a.shape[1]

    mean_list = []
    std_list =[]
    for i in range(n_col):
        mean_list.append(np.mean(a[:,i]))
        std_list.append(np.std(a[:,i]))
    a_s = np.zeros((n_row, n_col))
    for i in range(n_col):
        for j in range(n_row):
            a_s[j,i]=(a[j,i]-mean_list[i])/std_list[i]
    return a_s

def similarity(u,v):
    mag_u = magnitude(u)
    mag_v = magnitude(v)
    dot = dot_product(u,v)
    return dot/(mag_u * mag_v)

def magnitude(u):
    sum = 0
    for i in range(len(u)):
        sum = sum + u[i]**2
    return m.sqrt(sum)

def dot_product(u,v):
    d=0
    for i in range(len(u)):
        d=d+u[i]*v[i]
    return d
