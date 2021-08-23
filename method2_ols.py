
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 17:22:50 2021

@author: mohammed batis - 18511160002
"""


from numpy import *
from numpy.linalg import *

fr=open("ols_data.txt")
#LRdata_4variable.txt
lines=fr.readlines()
row=len(lines)
col=len(lines[0].split())
X=zeros((row,col-1))
Y=zeros((row,1))
fr.seek(0,0)

for i in range(row):
    line=fr.readline()
    print(line)
    line=line.split()
    
    for j in range(col-1):
        X[i][j]=float(line[j])
    Y[i][0]=float(line[col-1])
    
ave=average(X,axis=0)

X1=(X-ave)
X2=X1**2

A=zeros((col-1,col-1))
Y1=zeros((col-1,1))
for i in range(col-1):
    for j in range(col-1):
        A[i][j]=sum(X1[:,i]*X1[:,j])
    Y1[i][0]=sum(X1[:,i]*Y[:,0])

#w=dot(inv(A),Y1)
w=dot(linalg.pinv(A),Y1)

yave=average(Y,axis=0)
#print(yave)
ave=ave.reshape((col-1,1))
b0=yave-sum(w[:,0]*ave[:,0])
print("b0=",b0,w)
print("*"*40)
for i in range(row):
    #yhat=b0+w[0]*X[i][0]+w[1][0]*X[i][1]+w[2][0]*X[i][2]+w[3][0]*X[i][3]
    yhat=b0+sum(w[:,0]*X[i,:])
    print("Y real= %.2f, Y prediect =%.2f, Error Rate=%.2f"%(Y[i][0],yhat[0],yhat[0]-Y[i][0]))




