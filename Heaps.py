import heapq
myList=[9,5,4,1,3,2]

heapq.heapify(myList)  #turn myList into min heap 
print(myList)
print(myList[0])  # first value is always the smallest in the heap

#insert 10 in heap 
heapq.heappush(myList,10)
print(myList)
x = heapq.heappop(myList)  # pop and return smallest item
print(myList)

myList = [-val for val in myList] # multiply by -1 to negate
heapq.heapify(myList)
print(myList)

x = heapq.heappop(myList)
print(-x) # => 9 (making sure to multiply by -1 again)
