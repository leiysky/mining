from numpy import *
f = open('sample', 'r')
N = 80000
basic = 1/N
A = ndarray(shape=(N, N), dtype=int)
trust = [0 for i in range(0, N)]

for i in f.readlines():
    line = i.split('\t')
    a = int(line[0])
    trust[a+1] += 1
    b = int(line[1])
    A[b+1, a+1] = 1
    # print('from:',a,'to:',b)

print('first read complete')
f.close()

f = open('sample', 'r')

for i in f.readlines():
    line = i.split('\t')
    a = int(line[0])
    b = int(line[1])
    A[b+1, a+1] /= trust[a+1]

print('second read complete')
f.close()

for i in trust:
    if(i==0):
        for j in A[i]:
            A[j,i] = basic

d = 0.85
A = A * d + (1 - d) / N * zeros((N, N))
P0 = ones((N,1))  # P0代表Pn，为存储所有用户TR值的行向量
# P1 = []
P1 = A.dot(P0)  # P1代表Pn+1，为存储所有用户TR值的行向量
eps = 1e-6
n = 100
for i in range(100):
    print('iterate for %d times'%(i))
    P0 = P1
    P1 = A.dot(P1)

out = open('test100', 'w+')
print(P1)
out.write('uid\tTrustedRank\n')
for i in range(1,N):
    out.write('%d\t%e\n'%(i-1,P1[i,0]))
    
out.close()

