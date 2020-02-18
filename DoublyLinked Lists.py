#syntax for singly linked lists

'''removeSingle(Node Node,Node previousNode):
    tempNode = head
    while tempNode !=NULL:
        if tempNode == node:
            previousNode.nextNode = tempNode.nextNode
            tempNode = null
            return

        previousNode = tempNode
        tempNode = tempNode.nextNode'''

#syntax for doubly linked lists
removeDouble(Node node):
    node.previousNode.nextNode = node.nextNode
    node.nextNode.previousNode = node.previousNode
