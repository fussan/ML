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

i = np.identity(4)          #単位行列
print(i)

print(a.dtype)

j = np.array([1, 2, 3], dtype=float)
print(j.dtype)

k = np.array(j, dtype=complex)
print(k)

l = np.array([1, 2, 3, 4, 5], dtype=float)
print(l[3])

m = np.array([[11, 12, 13], [21, 22, 23]])
print(m.shape)
print(m[1, 2])

n = np.array([[1], [2], [3]])       #縦ベクトル
print(n)

o = np.array([[1, 2, 3]])           #横ベクトル
print(o)

