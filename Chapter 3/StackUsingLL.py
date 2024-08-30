class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        
    def isempty(self):
        if self.top == None: 
            return True
        else:
            return False

    def Push(self,data):
        if self.isempty():
            self.top = Node(data)
        else:
            temp = Node(data)
            temp.next = self.top
            self.top = temp

    def Pop(self):
        if self.isempty() == True:
            return None
        else:
            temp = self.top.data
            self.top = self.top.next
            return temp

    def display(self):
        if self.isempty()==True:
            return None
        else:
            temp = self.top
            while temp != None:
                print(temp.data)
                temp = temp.next        


S = Stack()
S.Push(30)
S.Push(40)
S.Push(50)
S.Push(60)
S.Push(70)
print(S.Pop())
print(S.Pop())
S.display()