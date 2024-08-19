class Node:
    def __init__(self, data):
        self.data = data
        self.nxt = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.top = -1


    def push(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.top += 1
        else:
            new_node = Node(data)
            self.tail.nxt = new_node
            self.tail = new_node
            self.top += 1
    

    def pop(self):
        if self.top == -1:
            print("The stack is empty")
        else:
            temp = self.head
            while temp.nxt != self.tail:
                temp = temp.nxt
            temp2 = self.tail
            self.tail = temp
            temp.nxt = None
            del temp2 
            self.top -= 1


    def get_top(self):
        assert self.top != -1 and self.tail != None, "The stack is empty"
        return f"Top index: {self.top} \nTop element: {self.tail.data}"


    def traverse(self):
        print("Stack: ", end=" ")
        temp = self.head
        while temp != None:
            print(temp.data, end=" | ")
            temp = temp.nxt
        # print(None)
        print()
    


stk = Stack()
l = [12, 33, 44, 55]
for i in l:
    stk.push(i)

print(stk.get_top())
stk.traverse()

print("\nAfter pop operation: ")
stk.pop()
stk.traverse()
print(stk.get_top())
