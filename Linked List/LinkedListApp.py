class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.nxt = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def insert_at_end(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data)
            new_node.prev = self.tail
            self.tail.nxt = new_node
            self.tail = new_node


    def insert_at_start(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.nxt = self.head
            self.head.prev = new_node
            self.head = new_node


    def insert_at_nth(self, data, pos):
        print(f"To insert {data} at position {pos}")
        temp = self.head
        if pos == 1:
            self.insert_at_start(data)
        elif pos == self.length()+1:
            self.insert_at_end(data)
        elif pos > self.length()+1:
            print("Length: ", self.length(), "--> Invalid index. Insertion is not possible")
        else:
            i = 1
            while i < pos-1:
                temp = temp.nxt
                i += 1
            new_node = Node(data)
            new_node.prev = temp
            new_node.nxt = temp.nxt
            temp.nxt.prev = new_node
            temp.nxt =new_node


    def delete_node(self, pos):
        print(f"To delete node at position {pos}")
        temp1 = self.head
        temp2 = temp1.nxt
        if pos == 1:
            self.head = temp2
            self.head.prev = None
            del temp1
        elif pos == self.length():
            temp = self.tail
            self.tail = temp.prev
            self.tail.nxt = None
            del temp
        elif pos > self.length():
            print("Length: ", self.length(), "--> Invalid index. Deletion is not possible")
        else:
            i = 1
            while i < pos-1:
                temp1 = temp1.nxt
                temp2 = temp2.nxt
                i += 1
            temp1.nxt = temp2.nxt
            temp2.nxt.prev = temp1
            print(f"{temp2.data} from index {pos} deleted")
            del temp2


    def find(self, data):
        temp = self.head
        found = False
        index = 1
        while temp != None:
            if temp.data == data:
                found = True
                return index
            temp = temp.nxt
            index += 1
        if not found:
            return f"{data} is not in the linked list"
    

    def data_at_index(self, pos):
        temp = self.head
        index = 1
        if pos > 0 and pos <= self.length():
            while index < pos:
                temp = temp.nxt
                index += 1
            return temp.data
        else:
            print("Invalid index")
        

    def length(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.nxt
        return count


    def traverse(self):
        temp = self.head
        print("Length: ", self.length())
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.nxt
        print("None")


    def reverse_traverse(self):
        temp = self.tail
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")



if __name__ == "__main__":
    ll = DoublyLinkedList()
    while (input("Exit? (y/n): ") != 'y'):
        choice = int(input("""
            Select command
            1. Insert at nth position
            2. Delete at nth position
            3. Search an element
            4. Find the element at a index
            5. Traverse the linked list
            6. Reverse traverse the linked list
        """))
        if choice == 1:
            ch = input("""Do you want to insert a list or a single element? 
                Here list will be appended at the end. (y/n):
            """)
            if ch == 'y':
                print("Insert a list: ")
                l = list(input().split())
                # l = list(map(int, input().split()))
                for i in l:
                    ll.insert_at_end(i)
            else:
                data = input("Data to insert: ")
                index = int(input("Index: "))
                ll.insert_at_nth(data, index)

        if choice == 2:
            index = int(input("Index: "))
            ll.delete_node(index)

        if choice == 3:
            ll.traverse()
            data = input("Data to find: ")
            print(f"{data} is at index: {ll.find(data)}")

        if choice == 4:
            idx = int(input("Enter index: "))
            print(f"Data at index {idx}: {ll.data_at_index(idx)}")

        if choice == 5:
            ll.traverse()

        if choice == 6:
            ll.reverse_traverse()