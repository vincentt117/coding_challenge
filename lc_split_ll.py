# https://leetcode.com/problems/split-linked-list-in-parts

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        size = 0
        head = root
        while head:
            size += 1
            head = head.next
        
        node_quant = ([(size // k) + 1] * (size % k)) + ([(size // k)] * (k-(size % k)))
        node_quant_idx = 0
        
        
        ret_list = []
        split_ptr = root
        to_add = root
        
        while node_quant_idx < len(node_quant):
            ret_list.append(to_add)
            to_add = None
            
            while node_quant[node_quant_idx] > 0:
                node_quant[node_quant_idx] -= 1
                if node_quant[node_quant_idx] == 0 and split_ptr:
                    hold = split_ptr
                    split_ptr = split_ptr.next
                    hold.next = None
                    to_add = split_ptr
                else:
                    split_ptr = split_ptr.next
                    
            node_quant_idx += 1 
            
        
        return ret_list
        
        