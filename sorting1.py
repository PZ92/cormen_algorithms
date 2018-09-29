# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 19:13:51 2018

@author: Pawel Zdunek
"""
#sorting examples from cormen
import random 

class MySorter():
    def __init__(self,n1,n2,A=[]):
        n1=n1
        n2=n2
        if A==[]:
            self.A=[random.randint(0,n1) for i in range(0,n2)]
        else:
            self.A=A
    def SortChecker(self,A,sorter=""):
        if A!=sorted(self.A):
            print(sorter, "failed")
        else:
            print(sorter, " ok ")    
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
        self.SortChecker(A, "Insertion Sort")
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
        MS(A,0,len(A)-1)
        self.SortChecker(A, "Merge Sort")
    def QuickSort(self):
        def Partition(A,l,r):
            pivot=A[r]
            i=l-1
            for j in range(l,r):
                if A[j]<=pivot:
                    i+=1
                    A[i],A[j]=A[j],A[i]
            A[i+1],A[r]=A[r],A[i+1]
            return i+1
        
        def QS(A,l,r):
            if l<r:
                q=Partition(A,l,r)
                QS(A,l,q-1)
                QS(A,q+1,r)
        A=self.A.copy()
        l=0
        r=len(A)-1
        QS(A,l,r)
        self.SortChecker(A, "Quick Sort")
    def QuickSort2(self): # 3 way, randomized QS
        def Partition(A,l,r):
            import random
            x=random.randint(l,r) 
            A[r],A[x]=A[x],A[r]
            pivot=A[r]
            i=l-1
            k=0# no of items equal to pivot 
            j=l
            while j<r-k:
                if A[j]==pivot:
                    k+=1
                    A[j],A[r-k]=A[r-k],A[j]

                if A[j]<pivot:
                    i+=1
                    A[i],A[j]=A[j],A[i]
                j+=1
            for x in range(0,k+1):
                A[i+1+x],A[r-x]=A[r-x],A[i+1+x]
            return i+1,k

        def QS(A,l,r):
            if l<r:
                q,k=Partition(A,l,r)
                QS(A,l,q-1)
                QS(A,q+1+k,r)
        A=self.A.copy()
        l=0
        r=len(A)-1
        QS(A,l,r)
        self.SortChecker(A,"Quicksort2")

import time            
x=MySorter(3,1000)

t1=time.time()
x.QuickSort2()
print(time.time()-t1)

t1=time.time()
x.QuickSort()
print(time.time()-t1)

t1=time.time()
x.MergeSort()
print(time.time()-t1)

t1=time.time()
x.InsertionSort()
print(time.time()-t1)



















