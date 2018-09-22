# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version == 4:
        return True
    return False
    
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = isBadVersion
        if n == 1:
            if b(1): return 1
            else: return
        if n == 2:
            for i in range(1, 3):
                if b(i): return i
        start = 1
        end = n
        ret = 0
        while start <= end:
            mid = int(start + (end - start) / 2)
            if mid == n: return mid
            if b(mid) and b(mid + 1) and b(mid-1): end = mid - 1
            elif not b(mid): start = mid + 1
            elif b(mid) and (not b(mid+1) or not b(mid-1)):
                ret = mid
                break
        return ret

s = Solution().firstBadVersion(5)
print(s)
