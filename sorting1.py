# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 19:13:51 2018

@author: Pawel Zdunek
"""
#sorting examples from cormen
import random 

class MySorter():
    def __init__(self,n1,n2):
        n1=n1
        n2=n2
        self.A=[random.randint(0,n1) for i in range(0,n2)]
        
#insertion sort
    def InsertionSort(self):
        A=self.A.copy()
        for j in range(1,len(A)):            
            key=A[j]
            i=j-1
            while i>=0 and A[i]>key:
                #print("--->",A,A[i],key)
                A[i+1]=A[i]
                i=i-1
            A[i+1]=key
        return A
#non increasing insertion sort
    def NonIncreasingIS(self):
        A=self.A.copy()
        for j in range(1,len(A)):
            key=A[j]
            i=j-1
            while i>=0 and A[i]<key:
                A[i+1]=A[i]
                i-=1
            A[i+1]=key
        return A
#mergesort
    def MergeSort(self,check_boolean=True):
        def Merge(A,p,q,r):
            L=[]
            R=[]
            for i in range(p,q+1):
                L.append(A[i])
            for i in range(q+1,r+1):
                R.append(A[i])
            i=0
            j=0
            for k in range(p,r+1):
                if i<len(L) and j<len(R):
                    if L[i]<R[j]:
                        A[k]=L[i]
                        i+=1
                    else:
                        A[k]=R[j]
                        j+=1
                else:
                    if i<len(L):
                        A[k]=L[i]
                        i+=1
                    if j<len(R):
                        A[k]=R[j]
                        j+=1
        def MS(A,p,r):
            if p<r:
                q=(p+r)//2
                MS(A,p,q)
                MS(A,q+1,r)
                Merge(A,p,q,r)
        
        
        A=self.A.copy()
        print(A)
        MS(A,0,len(A)-1)
        print(A)
        if A!=sorted(self.A) and check_boolean:
            print("the universe made MergeSort fail :(")
        return A
    
        
            
x=MySorter(10,20)

x.MergeSort()



















