# Problem -1 ----Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def isEmpty(self):
        return print(len(self.container) == 0)
    def size(self):
        return len(self.container)
def reverseString(s):
    stack = Stack()
    for ch in s:
        stack.push(ch)
    restr = ''
    while stack.size() != 0:
        restr += stack.pop()
    
    return restr


    
#Problem--2:Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0


if __name__ =='__main__' :
    print(reverseString('I am sakib'))
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))