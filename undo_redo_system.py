# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
       #point to old top

    def pop(self):
        if not self.top:
            return None
        removed_node = self.top
        self.top = self.top.next #move top to next node
        return removed_node.value 

    def peek(self):
        if self.top:
            return self.top.value
        else:
            return None
    def print_stack(self):
        current = self.top
        if not current:
            print("Stack is empty")
            return
        while current: 
            print(f"-{current.value}")
            current = current.next #update current to next value



def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            # Push action onto undo stack and clear redo stack
            undo_stack.push(action)
            redo_stack = Stack()  # clear redo by replacing with a new Stack
            print(f"Action performed: {action}")

        elif choice == "2":
            # Pop action from undo stack and push it onto redo stack
            action = undo_stack.pop()
            if action is None: 
                print("No actions to undo")
            else: 
                redo_stack.push(action)
                print(f"Undid action: {action}")

        elif choice == "3":
            # Pop action from redo stack and push it onto the undo stack
            action = redo_stack.pop()
            if action is None:
                print("No actions to redo")
            else:
                undo_stack.push(action)
                print(f"Redid action: {action}")

        elif choice == "4":
            print("\nUndo Stack (top first):")
            undo_stack.print_stack()

        elif choice == "5":
            print("\nRedo Stack (top first):")
            redo_stack.print_stack()

        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    run_undo_redo()

#When working with the undo/redo system, the most recent action is the first one you undo or redo, and with stacks being last-in
#first-out, this works for the undo/redo functionality perfectly, as the most recent action is always on top of the stack.
#When the action is undone, it is pushed onto a second stack for redo operations, which reflects the efficiency of the undo/redo
# system and why stacks are used with undo/redo systems. Queues are better for help desks because, unlike stacks, they are 
# first-in, first-out. This means the first request is handled first, which matches the efficiency needed for a help desk 
# environment, think of it like a customer waiting in line or a restaurant. These both differ from Python lists in that, 
# unlike first-in, first-out or last-in, first-out, Python lists don’t follow those formats and allow users to insert, 
# remove, undo and redo any information at any point in the list instead of modifying the first or the last. In other words, 
# Python lists can implement both first-in, first-out and last-in, first-out procedures. Stacks and queues can be better for 
# handling data structure for specific operations as was proved in this assignment and can help to prevent errors in data 
# handling because of the restrictions.
