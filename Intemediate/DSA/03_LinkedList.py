# has data and next which can be doubly (prev) and circular (last and start is not null)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def traverse(head):
        currentNode = head
        while currentNode:
            print(currentNode.data, end = '->')
            currentNode = currentNode.next
        print('Null')
    
    def findLowestValue(head):
        minValue = head.data
        currentNode = head.next
        while currentNode:
            if currentNode.data < minValue:
                minValue = currentNode.data
            currentNode = currentNode.next
        return minValue
    
    def deleteSpecificNode(head, nodeToDelete):
        if head == nodeToDelete:
            return head.next

        currentNode = head
        while currentNode.next and currentNode.next != nodeToDelete:
            currentNode = currentNode.next

        if currentNode.next is None:
            return head

        currentNode.next = currentNode.next.next

        return head
    
    def insertNodeAtPosition(head, newNode, position):
        if position == 1:
            newNode.next = head
            return newNode

        currentNode = head
        for _ in range(position - 2):
            if currentNode is None:
             break
            currentNode = currentNode.next

        newNode.next = currentNode.next
        currentNode.next = newNode
        return head
        
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

Node.traverse(node1)
print(Node.findLowestValue(node4))
Node.deleteSpecificNode(node1,node2)
Node.traverse(node1)

newNode = Node(97)
node1 = Node.insertNodeAtPosition(node1, newNode, 2)

Node.traverse(node1)