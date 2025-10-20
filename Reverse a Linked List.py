class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # Store next node
        current.next = prev       # Reverse pointer
        prev = current            # Move prev forward
        current = next_node       # Move current forward

    return prev  # New head
# Create linked list: 1 -> 2 -> 3 -> None
head = ListNode(1, ListNode(2, ListNode(3)))
new_head = reverse_linked_list(head)
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
