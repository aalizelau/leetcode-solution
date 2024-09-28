def merge(nums1, m, nums2, n):
    mergedpointer  = m+n-1
    pointer1 = m-1
    pointer2 = n-1

    
    while pointer2 >=0:
        nums1[mergedpointer] = nums2[pointer2]
        pointer2 -=1
        mergedpointer -=1
    while pointer1 and pointer2 >=0:
        if nums1[pointer1] > nums2[pointer2]:
            nums1[mergedpointer] = nums1[pointer1]
            pointer1 -=1 
        else:
            nums1[mergedpointer] = nums2[pointer2]
            pointer2 -=1
        mergedpointer -=1