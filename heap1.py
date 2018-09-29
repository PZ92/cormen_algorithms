
info="""
	heap is a nearly complete binary tree - completely filled at all levels except deepest one 
	which is filled from left up to a point 
	two attributes:
		heap.length  -> no of elements in array
		heap.heap-size -> how many elements in heap are stored within array A 

		if root is 1 indexed -> A[1]
		for any node i:
		 its parent is i//2 (floor i/2)
		 left child is 2i
		 right child is 2i+1

	two kinds of binary heaps:
		max-heaps -> have max-heap property: A[Parent[i]]>= A[i] -> largest element in the root 
		min-heaps -> have min-heap property: A[Parent[i]]<= A[i] -> smallest element at root

	for heap-sort algorithm we use max-heaps 
	min-heaps commonly implement priority ques

	height of node -> no of edges from node to leaf
	height of heap -> height of root node 
	height of n-element tree is O(lg(n)) because its a complete binary tree

	Procedures:
		MAX-HEAPIFY - O(lg(n)) -> key to maintaining max-heap property
		BUILD-MAX-HEAP - linear time, produces max-heap from unsorted input array
		HEAPSORT - 0(n(lg(n))) sorts array in place
			those allow heap to implement priority queue, are 0(lg(n))
		MAX-HEAP-INSERT
		HEAP-EXTRACT-MAX
		HEAP-INCREASE-KEY
		HEAP-MAXIMUM 
"""

class MyFirstHeap():
	def __init__(self,n1=20,n2=10):
		import random
		self.A=[random.randint(0,n1) for i in range(0,n2)]
		self.A=[16,4,10,14,7,9,3,2,8,1]
		self.A=[len(self.A)]+self.A #storing heapsize in 0th element 

		self.A=[27,17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
		self.A=[4,1,3,2,16,9,10,14,8,7]
		self.A=[len(self.A)]+self.A
	def info():
		print("my first heap with default ",n1, " elements in range 0 to ",n2)
		print("heap is 1 indexed")

	def LEFT(self,i):
		return 2*i
	def RIGHT(self,i):
		return 2*i+1
	def PARENT(self,i):
		if i==1:
			return 0
		return i//2

	def MAXHEAPIFY(self,A,i):
		#assumes that trees rooted at l and r are max-heaps
		def heapsize(A):
			return A[0]
		l=self.LEFT(i)
		r=self.RIGHT(i)
		if l<=heapsize(A) and A[l]>A[i]:
			largest=l
		else:
			largest=i 
		if r<=heapsize(A) and A[r]>A[largest]:
			largest=r
		if largest !=i:
			A[i],A[largest]=A[largest],A[i]
			self.MAXHEAPIFY(A,largest)

	def BUIILDMAXHEAP(self,A):
		i=A[0]//2
		while i!=0:
			self.MAXHEAPIFY(A,i)
			print(A)
			i-=1






x=MyFirstHeap()
print(x.A)
x.BUIILDMAXHEAP(x.A)
print(x.A)