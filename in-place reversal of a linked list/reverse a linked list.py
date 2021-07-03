class Node:
    def __init__(self, val, next=None):
        self.next = next
        self.val = val
    
def solution(head):
    
    curr = head
    prev = None
    
    while curr != None:
        curr_next = curr.next #this keeps track of next node to eventually set curr to it -- can't just do curr.next because you set curr.next to prev in order to reverse the current node
        curr.next = prev
        prev = curr
        curr = curr_next

    return prev.val, prev.next.val, prev.next.next.val, prev.next.next.next.val, prev.next.next.next.next
    
def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next = Node(8)
    head.next.next.next = Node(10)
    
    print(head.val, head.next.val, head.next.next.val, head.next.next.next.val, head.next.next.next.next)
    print(solution(head))
    
main()