class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None

        node = head
        # 遍历链表,构造新结点插入原链表
        while node != None:
            newnode = RandomListNode(node.label)
            newnode.next = node.next
            node.next = newnode
            node = newnode.next

        # 遍历链表，根据原结点的随机指针，给新加入的结点赋值
        node = head
        newhead = head.next
        while node != None and node.next != None:
            newnode = node.next
            if node.random != None:
                newnode.random = node.random.next
            else:
                newnode.random = None
            node = newnode.next

        # 遍历链表, 将原有的结点从链表中摘出
        node = head
        while node != None and node.next != None:
            newnode = node.next
            node.next = newnode.next
            if node.next != None:
                newnode.next = node.next.next
            else:
                newnode.next = None
            node = node.next
        return newhead