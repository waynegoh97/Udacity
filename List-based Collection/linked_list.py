#linked list is used to quickly add and drop items.
#Singly linked list means that the current node knows the pointer of the next element
#Compared to normal list in python, list.append() takes O(1), but list.pop() takes O(n).
#Linked list takes O(1) to add and drop items in a queue. 

#Linked lists are best used in FIFO queue
#Stack LIFO when implemented using linked list have similar performance as normal list

#Implementing Queue using collections deque (pronounce as deck)
#It is used to implement linked list

from collections import deque

#llist = deque(['a','b','c']) #create a linked list
llist = deque() #create empty linked list
llist.append('Andy')
llist.append('Susan')
llist.append('Tom')
print("Current queue: {}".format(llist))

llist.popleft()

print("Current queue: {}".format(llist))

#Implementing Stack using collections deque
#Stack example is the back button on internet

llist = deque()
llist.appendleft("https://www.google.com")
llist.appendleft("https://www.facebook.com")
llist.appendleft("https://www.youtube.com")

print("History websites: {}".format(llist))
llist.popleft()
print("History website: {}".format(llist))

#Implementing linked list from scratch

class LinkedList:
    def __init__(self):
        self.head = None
        