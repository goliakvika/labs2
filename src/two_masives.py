def is_subarray(nums1, nums2):
    if not nums1:
        return True
    i = 0
    j = 0
    while j < len(nums2):
        if nums1[i] == nums2[j]:
            i += 1
            if i == len(nums1):
                return True
        j += 1

    return False



nums1_1 = [1, 2, 3]
nums2_1 = [1, 2, 3, 4]
print(is_subarray(nums1_1, nums2_1))  # True

nums1_2 = [4, 2]
nums2_2 = [1, 2, 3, 4]
print(is_subarray(nums1_2, nums2_2))  # False

nums1_3 = [1, 3, 5]
nums2_3 = [1, 2, 3, 4, 5]
print(is_subarray(nums1_3, nums2_3))  # True




