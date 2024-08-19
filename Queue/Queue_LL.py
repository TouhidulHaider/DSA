class Node:
    def __init__(self, data):
        self.data = data
        self.nxt = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.rear = -1
        self.front = -1


    def enqueue(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.front = 0
            self.rear += 1
        else:
            self.tail.nxt = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.rear += 1


    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty")
        else:
            temp = self.head

            if self.front == self.rear:
                print(f"{temp.data} dequeued.")
                self.front += 1
                self.head = None
                self.tail = None
                del temp
            else:
                self.head = temp.nxt
                self.head.prev = None
                self.front += 1
                print(f"{temp.data} dequeued.")
                del temp


    def isEmpty(self):
        if (self.front > self.rear) and self.head is None:
            return True
        else:
            return False


    def peak(self):
        # Returns the element at the front of the queue without removing it.
        if self.isEmpty():
            print("The queue is empty")
        else:
            print("The peak elememt is ", self.head.data)

    def stack_info(self):
        print(f"Rear index: {self.rear}")
        print(f"Front index: {self.front}")
        print(f"The length the stack is {(self.rear - self.front)+1}")
        if not self.isEmpty():
            print(f"Peak element: {self.head.data}")
            print(f"Last element: {self.tail.data}")


    def traverse(self):
        print(f"Front index:{self.front}, Rear index: {self.rear}")
        temp = self.head
        print("Queue:", end=" ")
        while temp is not None:
            print(temp.data, end=" | ")
            temp = temp.nxt
        print("\n\n")
    


# driver code
if __name__ == "__main__":
    q = Queue()
    l = [11, 22, 33, 44, 55, 66, 77]

    for i in l:
        q.enqueue(i)

    q.traverse()
    q.dequeue()
    q.traverse()
    q.peak()
    q.stack_info()

    q.enqueue(88)
    q.enqueue(99)

    for _ in range(10):
        q.dequeue()
        q.traverse()

    q.stack_info()
