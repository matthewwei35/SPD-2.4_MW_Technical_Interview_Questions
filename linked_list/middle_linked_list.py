# Given a single-linked list, find the middle value in the list.

def middle_linked_list(head):
  slow, fast = head, head
  while fast and fast.next != None:
    slow = slow.next
    fast = fast.next.next
  return slow
