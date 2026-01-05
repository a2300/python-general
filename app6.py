class UndoStack:
    def __init__(self):
        self.stack = []
    
    def push_action(self, action):
        self.stack.append(action)

    def undo(self):
        if self.stack:
            return self.stack.pop()
        return None
    
    def is_empty(self):
        return len(self.stack) == 0
    

undoStack = UndoStack()
undoStack.push_action({"id": 1, "type": "type", "value": "Hello, World!"})
undoStack.push_action({"id": 2, "type": "delete", "value": "o"})

print(undoStack.undo())

