import numpy as np

def Pmax(a):
    n = len(a)
    if(len(a) == 1):
        return a[0]
    if(len(a) == 2):
        return max(a[0],a[1])

    return max(Pmax(a[:n//2]),Pmax(a[n//2:]))

def Pmin(a):
    n=len(a)
    if(len(a) == 1):
        return a[0]
    if(len(a) == 2):
        return min(a[0],a[1])

    return min(Pmin(a[:n//2]),Pmin(a[n//2:]))


a = np.random.randint(low=1, high=100, size=7).tolist()
print(a)
print(Pmax(a))
print(Pmin(a))
