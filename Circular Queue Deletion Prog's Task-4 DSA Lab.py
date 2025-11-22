class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty! Cannot delete from beginning.")
            return
        deleted_data = self.head.data
        self.head = self.head.next
        print(f"Node with data '{deleted_data}' deleted from beginning.")
    def delete_from_end(self):
        if self.head is None:
            print("List is empty! Cannot delete from end.")
            return
        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            print(f"Last node with data '{deleted_data}' deleted.")
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next    
        deleted_data = temp.next.data
        temp.next = None
        print(f"Node with data '{deleted_data}' deleted from end.")
    def display(self):
        if self.head is None:
            print("List is empty!")
            return
        temp = self.head
        output = []
        while temp:
            output.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(output) + " -> None")
#--Testing the linked list--
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
print("Original List:")
ll.display()
ll.delete_from_beginning()
print("After deleting from beginning:")
ll.display()
ll.delete_from_end()
print("After deleting from end:")
ll.display()
ll.delete_from_beginning()
print("After a second delete from beginning:")
ll.display()
