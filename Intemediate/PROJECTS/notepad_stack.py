# undo_stack_notes.py

class Notepad:
    def __init__(self):
        self.notes = []
        self.undo_stack = []

    def add_note(self, note):
        self.notes.append(note)
        self.undo_stack.append(('add', note))

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        action, note = self.undo_stack.pop()
        if action == 'add':
            self.notes.remove(note)

    def show_notes(self):
        if not self.notes:
            print("No notes.")
        for i, note in enumerate(self.notes, 1):
            print(f"{i}. {note}")

# Demo
n = Notepad()
n.add_note("Learn Python")
n.add_note("Write a blog post")
n.show_notes()
n.undo()
n.show_notes()
