    # Python program to convert infix expression to postfix

    # Class to convert the expression

class node:
    def __init__(self,next = None,data = None) -> None:
        self.head == next
        self.data = data
    
def push(headref,data):
    pointer1=node()
    pointer1.data=data
    pointer1.next = headref

    if(headref!=None):
        temp = headref
        while(temp.next != headref):
            temp = temp.next
        temp.next = pointer1
    else:
        pointer1.next =pointer1
    headref=pointer1
    return headref
    

class Conversion:

    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.head = None
        # Precedence setting
        self.output = None
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # check if the stack is empty
    def isEmpty(self):
        return True if self.head == None else False

    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]

    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    # Push the element to the stack
    # def push(self, op):
    #     self.top += 1
    #     self.array.append(op)

    # A utility function to check is the given character
    # is operand
    def isOperand(self, ch):
        return ch.isalnum()

    # Check if the precedence of operator is strictly
    # less than top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    # The main function that
    # converts given infix expression
    # to postfix expression
    def infixToPostfix(self, exp):

        # Iterate over the expression for conversion
        for i in exp:
            # If the character is an operand,
            # add it to output
            if self.isOperand(i):
                push(self.output,i)

            # If the character is an '(', push it to stack
            elif i == '(':
                push(self.head,i)

            # If the scanned character is an ')', pop and
            # output from the stack until and '(' is found
            elif i == ')':
                while ((not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()

            # An operator is encountered
            else:
                while (not self.isEmpty() and self.notGreater(i)):
                    # this is to pass cases like a^b^c
                    # without if ab^c^
                    # with if abc^^
                    if i == "^" and self.array[-1] == i:
                        break
                    self.output.append(self.pop())
                self.push(i)

        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())

        print(" ".join(self.output))


    # Driver's code
if __name__ == '__main__':
    exp = "a+2*(c^d-e)^(f+g*h)-i"
    obj = Conversion(len(exp))

    # Function call
    obj.infixToPostfix(exp)

    # This code is contributed by Nikhil Kumar Singh(nickzuck_007)
