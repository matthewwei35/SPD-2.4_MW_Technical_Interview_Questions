# Given two sorted linked lists, merge them so that the resulting linked list is also sorted.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_list(list1, list2):
    if list1 is None and list2 is None:
        return None
    elif list1 is None and list2 is not None:
        return list2
    elif list2 is None and list1 is not None:
        return list1

    pointer1 = list1
    pointer2 = list2
    merge_list = ListNode()
    tail = merge_list

    while pointer1 is not None and pointer2 is not None:
        if pointer1.val > pointer2.val:
            new_node = ListNode(pointer2.val)
            tail.next = new_node
            tail = tail.next
            pointer2 = pointer2.next 
        elif pointer1.val <= pointer2.val:
            new_node = ListNode(pointer1.val)
            tail.next = new_node
            tail = tail.next
            pointer1 = pointer1.next 

    if pointer1 is not None:
        tail.next = pointer1
    elif pointer2 is not None:
        tail.next = pointer2
    return merge_list.next
