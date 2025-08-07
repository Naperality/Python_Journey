# task_linkedlist.py

class TaskNode:
    def __init__(self, task):
        self.task = task
        self.next = None

class ToDoList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = TaskNode(task)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def show_tasks(self):
        curr = self.head
        if not curr:
            print("No tasks.")
            return
        i = 1
        while curr:
            print(f"{i}. {curr.task}")
            curr = curr.next
            i += 1

# Demo
todo = ToDoList()
todo.add_task("Buy groceries")
todo.add_task("Walk the dog")
todo.show_tasks()
