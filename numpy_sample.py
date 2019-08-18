import numpy as np
import scipy as sp

a = np.array([1, 2, 3])     #リスト
print(a)

b = np.array((10, 20, 30))  #タプル（要素の変更不可)
print(b)

c = np.array([[1.5, 0], [0, 3.0]])
print(c)

d = d = np.array([a, b])
print(d)

e = np.zeros(3)
print(e)

f = np.ones((3, 4))         #引数はタプルにする
print(f)

g = np.empty(3)
print(g)

h = np.zeros_like(c)
print(h)

i = np.identity(4)
print(i)