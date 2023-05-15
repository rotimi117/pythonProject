from collections import deque

queue1 = deque([])
queue1.append(1)
queue1.append(2)
queue1.append(3)
queue1.append(4)
queue1.append(5)
queue1.append(6)
print(queue1)

queue1.popleft()
print(queue1)