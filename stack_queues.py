from collections import deque
q = deque()          # empty
q=deque([12,15,5])
q.append(4) #append to right side 
q.appendleft(6)
print(q)

x=q.pop()
y=q.popleft()

print(x)
print(y)
print(q)

q.rotate(12)
print(q)