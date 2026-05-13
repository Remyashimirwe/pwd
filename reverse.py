# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    """
    Add two numbers represented as linked lists in reverse order.
    
    Args:
        l1: ListNode representing first number (reversed)
        l2: ListNode representing second number (reversed)
    
    Returns:
        ListNode representing sum (reversed)
    
    Examples:
        l1 = [2,4,3], l2 = [5,6,4] → [7,0,8] (342 + 465 = 807)
        l1 = [0], l2 = [0] → [0]
        l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] → [8,9,9,9,0,0,0,1]
    """

    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:

        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        current.next = ListNode(total % 10)
        carry = total // 10
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        current = current.next
    
    return dummy.next


# Helper function to create linked list from list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to print linked list
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Test cases
if __name__ == "__main__":
    # Test 1: 342 + 465 = 807
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = addTwoNumbers(l1, l2)
    print(f"Test 1: {print_linked_list(result)}")
    print(f"Expected: [7, 0, 8]\n")
    
    # Test 2: 0 + 0 = 0
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = addTwoNumbers(l1, l2)
    print(f"Test 2: {print_linked_list(result)}")
    print(f"Expected: [0]\n")
    
    # Test 3: 9999999 + 9999 = 10009998
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = addTwoNumbers(l1, l2)
    print(f"Test 3: {print_linked_list(result)}")
    print(f"Expected: [8, 9, 9, 9, 0, 0, 0, 1]\n")