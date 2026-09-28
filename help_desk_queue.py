# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue: 
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.head:
           self.head = new_node
           self.tail = new_node
        else:
           self.tail.next = new_node
           self.tail = new_node

    def dequeue(self):
        if not self.head:
           return None
        removed_node = self.head
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return removed_node.value

    def peek(self):
        return self.head.value if self.head else None

    def print_queue(self):
        current = self.head
        if not current:
            print("Queue is empty")
            return
        while current:
            print(f"-{current.value}")
            current = current.next #update current to next value

    


def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()
   

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")
        #add customer to the queue
        if choice == "1":
            name = input("Enter customer name: ")
            queue.enqueue(name)
            print(f"{name} added to the queue.")

        #help next customer in the queue and return their name
        elif choice == "2":
            next_customer = queue.dequeue()
            if next_customer is None:
                print("No customers in the queue.")
            else:
                print(f"Helping customer: {next_customer}")

        #view the next customer in the queue without removing them
        elif choice == "3":
            next_customer = queue.peek()
            if next_customer is None:
                print("No customers in the queue.")
            else:
                print(f"Next customer: {next_customer}")

        #view all customers in the queue without removing them
        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_queue()


        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
