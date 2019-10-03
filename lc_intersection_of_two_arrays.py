class Solution:
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     if len(nums1) < len(nums2):
    #         min_set = set(nums1)
    #         target = nums2
    #     else:
    #         min_set = set(nums2)
    #         target = nums1
    #     inter_set = set()
    #     for num in target:
    #         if num in min_set:
    #             inter_set.add(num)
    #     return list(inter_set)
    
    # w/o using sets
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n1index = 0
        n2index = 0
        intersection = []
        while n1index < len(nums1) and n2index < len(nums2):
            if nums1[n1index] == nums2[n2index]:
                if not intersection or not intersection[-1] == nums1[n1index]:
                    intersection.append(nums1[n1index])
                n1index += 1
                n2index += 1
            elif nums1[n1index] > nums2[n2index]:
                n2index += 1
            elif nums1[n1index] < nums2[n2index]:
                n1index += 1
        return intersection
            
            
        