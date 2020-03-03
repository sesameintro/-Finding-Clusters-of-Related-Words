import numpy as np
import copy as cp

def Normalization(Data):
    n,m = np.shape(Data)
    maxx = max(Data[:,0])
    maxy = max(Data[:,1])
    minx = min(Data[:,0])
    miny = min(Data[:,1])
    Minx = np.ones((n,1)) * minx

    Miny = np.ones((n,1)) * miny
    N1 = (np.asarray(Data[:,0]).reshape((n,1)) - Minx)/(maxx-minx)
    N2 = (np.asarray(Data[:,1]).reshape((n,1)) - Miny)/(maxy-miny)
    Norm = np.concatenate((N1,N2),axis=1)
    return Norm



