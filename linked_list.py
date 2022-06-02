from collections import deque
ll=deque()
# 85 15 4 20
ll.append(85)
ll.append(15)
ll.append(4)
ll.append(20)

ll.reverse()
print(*ll)
for e in ll:
    print(e)