class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d2 = {}
        result = []
        min_index = -1
        for i in range(len(list2)):
            d2[list2[i]] = i
        for i in range(len(list1)):
            if list1[i] in d2:
                min_index = i + d2[list1[i]]
                break
        for i in range(len(list1)):
            if list1[i] in d2 and i + d2[list1[i]] < min_index:
                result = [list1[i]]
                min_index = i + d2[list1[i]]
            if list1[i] in d2 and i + d2[list1[i]] == min_index:
                result += [list1[i]]
        return result