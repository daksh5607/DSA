class FixedSizeQueue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def enqueue(self, request_id):
        if self.is_full():
            print(f"Queue is full. Cannot enqueue request {request_id}.")
            return False
        
        self.queue.append(request_id)
        print(f"Enqueued request: {request_id}")
        return True

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        
        removed_id = self.queue.pop(0)
        print(f"Dequeued request: {removed_id}")
        return removed_id

    def size(self):
        return len(self.queue)

    def is_full(self):
        return self.size() == self.capacity
    
    def is_empty(self):
        return self.size() == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

print("--- Initializing Queue ---")
ticket_queue = FixedSizeQueue(capacity=3) 

print("\n--- Testing Enqueue ---")
ticket_queue.enqueue("T101")
ticket_queue.enqueue("T102")
ticket_queue.enqueue("T103")

print(f"Current Queue Size: {ticket_queue.size()}")
print(f"Is Queue Full? {ticket_queue.is_full()}")

ticket_queue.enqueue("T104")

print("\n--- Testing Dequeue ---")
next_ticket = ticket_queue.dequeue()
print(f"Next to be processed (peek): {ticket_queue.peek()}")
next_ticket = ticket_queue.dequeue()

print(f"Current Queue Size: {ticket_queue.size()}")
print(f"Is Queue Full? {ticket_queue.is_full()}")

ticket_queue.enqueue("T105")

ticket_queue.dequeue()
ticket_queue.dequeue()

ticket_queue.dequeue()
print(f"Is Queue Empty? {ticket_queue.is_empty()}")
