from stack import Stack

class Queue: 
    def __init__(self):
        self.stack_in = Stack() 
        self.stack_out = Stack() 

    def enqueue(self, data):
        self.stack_in.push(data)

    def dequeue(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        if self.stack_out.is_empty():
            raise IndexError("Fila vazia")
        return self.stack_out.pop()

    def is_empty(self):
        return self.stack_in.is_empty() and self.stack_out.is_empty()