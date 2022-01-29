import sys
from collections import deque
class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = deque()
    
    def pushCharacter(self, data):
        # take data and put them in the list; stack method
        self.stack.append(data)
    
    def enqueueCharacter(self, data):
        # Take data and put them in the deque; Queue method
        self.queue.append(data)
    
    def popCharacter(self):
        # Take out one character from the list from right; Stack Method
        return self.stack.pop()
    
    def dequeueCharacter(self):
        # Take out one character from the deque from left; Queue method
        return self.queue.popleft()

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    