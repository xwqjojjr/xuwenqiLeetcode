class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        j = k = i= 0
        res = []
        #print len(nums1)
        l = len(nums1)+len(nums2)
        while i < len(nums1)+len(nums2):
            while (j == len(nums1)):
                print "触发成功"
                res = res + nums2[k:]
                if l%2 == 1:
                    return res[l/2]
                else:
                    print res
                    return (res[l/2-1]+res[l/2])/2.0
            while k == len(nums2):
                res = res + nums1[j:]
                if l%2 == 1:
                    return res[l/2]
                else:
                    print res
                    return (res[l/2-1]+res[l/2])/2.0
            if(nums1[j] >= nums2[k]):
                #print k,j
                res.append(nums2[k])
                k = k+1
               # print res[i]
            else:
               # print i,j,nums1[j]
                res.append(nums1[j])
                j = j+1
            i = i+1
            #print "j=",j,"k =",k,"nums1 =",nums1[j],"nums2 = ",nums2[k],"res=",res
        print res
