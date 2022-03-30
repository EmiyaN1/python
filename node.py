class Node():
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext): #将新节点的next引用指向当前list中的节点
        self.next = newnext


class Unordered():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp       #修改列表头节点，使其指向新创建的节点


    def length(self):
        current = self.head
        count=0
        while current !=None:
            count = count + 1
            current = current.getNext()
        return count


    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getNext()==item:
                found=True
            else:
                current = current.getNext()
        return found




