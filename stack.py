class Stack:
    # top index = end of list
    def __init__(self):
        self._stack_lst = []
        
    def __str__(self):
        return f'{self._stack_lst}'
    
    def __repr__(self):
        return f'Stack()'
    
    def get_lst(self):
        return self._stack_lst.copy()
    
    def push(self, element):
        self._stack_lst.append(element)
    
    def pop(self):
        if len(self._stack_lst) != 0:
            return self._stack_lst.pop()
        else:
            print('The stack is empty')
            return None
    
    def top(self):
        if len(self._stack_lst) != 0:
            return self._stack_lst[0]
        else:
            print('The stack is empty')
            return None
        
    def is_empty(self):
        return len(self._stack_lst) == 0
    
    def __len__(self):
        return len(self._stack_lst)