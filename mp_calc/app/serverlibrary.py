


def mergesort(arr, key=lambda item: item.username):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    mergesort(left)
    mergesort(right)

    i = j = k = 0
    
    while i < len(left) and j < len(right):
        print(key(left[i]))
        print(key(right[i]))

        if key(left[i]) <= key(right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr
    pass

class Stack:
    
    # initialize an empty list for the stack to store the items
        def __init__(self):
            self.__items = []
        
        # stores an Integer into the top of the stack
        def push(self, item):
            self.__items.append(item)

        # returns and removes the top element of the stack.
        # Return value is optional as it may return None if there are no more elements in the stack.
        def pop(self):
            if len(self.__items) >= 1:
                return self.__items.pop()
        
        # returns the top element of the stack. If the stack is empty, it returns None
        def peek(self):
            if len(self.__items) >= 1:
                return self.__items[0]
        
        # returns either true or false depending whether the stack is empty or not
        @property
        def is_empty(self):
            return self.__items == []
        
        # returns the number of items in the stack
        @property
        def size(self):
            return len(self.__items)

class EvaluateExpression:
    valid_char = '0123456789+-*/() '
    def __init__(self, string=""):
        self.expr = string
        pass

    @property
    def expression(self):
        print(self.expr)
        return self.expr
        pass

    @expression.setter
    def expression(self, new_expr):
        for x in new_expr:
            if x not in self.valid_char:
                self.expr = ""
                return
            else:
                self.expr = new_expr
        pass 
    
    def insert_space(self):
        oplist = '+-*/()'
        templist = []
        temp = ""
        for x in self.expr:
            templist.append(x)
        for x in range(len(templist)):
            if templist[x] in oplist:
                templist[x] = " " + templist[x] + " "
        for x in templist:
            temp+=x
        return temp
        pass
    
    def process_operator(self, operand_stack, operator_stack):
        oplist = '+-*/'
        item = operator_stack.pop()
        if item in oplist:
            op1 = int(operand_stack.pop())
            op2 = int(operand_stack.pop())
            def process_op(op1,op2,op):
                if op == "+":
                    return op2+op1
                elif op == "-":
                    return op2-op1
                elif op == "*":
                    return op1*op2
                elif op == "/":
                    return op2//op1
                else:
                    return 0
            x = process_op(op1, op2, item)
            operand_stack.push(x)
        else:
            operator_stack.pop()
        ans = operand_stack.peek()
        return ans
    
    def evaluate(self):
        operand_stack = Stack()
        operator_stack = Stack()
        expression = self.insert_space()
        tokens = expression.split()
        oplist = '+-*/'
        operands = "0123456789"
        for x in tokens:
            if x in operands:
                operand_stack.push(x)
            elif x=="-" or x =="+":
                while operator_stack.size != 0 and operator_stack.peek() != "(" and operator_stack.peek() != ")" :
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(x)
            elif x=="*" or x=="/":
                while operator_stack.size != 0 and (operator_stack.peek() == "*" or operator_stack.peek() == "/") :
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(x)
            elif x=="(":
                operator_stack.push(x)
            elif x==")":
                self.process_operator(operand_stack, operator_stack)
        while operator_stack.size != 0:
            if operator_stack.peek()!=("(" or ")"):
                self.process_operator(operand_stack, operator_stack)
            else:
                operator_stack.pop()
        final = operand_stack.pop()
        print(final)
        return final
        pass

def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





