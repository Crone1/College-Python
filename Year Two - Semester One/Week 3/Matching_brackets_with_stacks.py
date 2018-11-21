def check_brackets(line):
    class Stack(object):

        def __init__(self):
              self.stack = []
              self.top = 0
    
        def is_empty(self):
          return self.top == 0
    
        def push(self, item):
          if self.top < len(self.stack):
             self.stack[self.top] = item
          else:
             self.stack.append(item)
    
          self.top += 1
    
        def pop(self):
          if self.is_empty():
             return None
          else:
             self.top -= 1
             return self.stack[self.top]
             
    shtack = Stack()
    for c in line:
        if c == '(':
            shtack.push(c)
            
            
        elif c == ')' and shtack.is_empty():
            return False
            
        elif c == ')' and not shtack.is_empty():
            shtack.pop()
            

    return shtack.is_empty()