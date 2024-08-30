class Node:
    def __init__(self, v = None):
        self.value = v
        self.next = None
        return
    def isempty(self):
        if self.value == None:
            return(True)
        else:
            return(False)
    # recursive
    def append(self,v):
        # If current node is empty
        if self.isempty(): 
            self.value = v
        # If current node is last node of the list 
        elif self.next == None:
            self.next = Node(v)
        # Else raverse to next node
        else:
            self.next.append(v) 
        return
    # append, iterative
    def appendi(self,v):
        # if current node is empty 
        if self.isempty():
            self.value = v
            return
        temp = self
        # Traverse the list to find the last node
        while temp.next != None:
            temp = temp.next
        temp.next = Node(v) 
        return
    def insert(self,v):
        if self.isempty():
            self.value = v
            return
        newnode = Node(v)
        # Exchange values in self and newnode
        (self.value, newnode.value) = (newnode.value, self.value)
        # Switch links
        (self.next, newnode.next) =(newnode, self.next)
        return
    # delete, recursive
    def delete(self,v):
        # If list is empty
        if self.isempty():
            return
        # If v is the current node of the list
        if self.value == v:
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            return
        else:
            if self.next != None:
                self.next.delete(v)
                if self.next.value == None:
                    self.next = None
        return
    def display(self):
        if self.isempty()==True:
            print('None')
        else:
            temp = self
            while temp!=None:
                print(temp.value,end="  ")
                temp = temp.next
head = Node(10)
head.append(20)
head.append(30)
head.appendi(40)
head.appendi(50)
head.delete(30)
head.display()