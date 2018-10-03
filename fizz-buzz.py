class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n + 1):
            res.append(str(i))
            if i % 3 == 0 and i % 5 == 0: res[i - 1] = "FizzBuzz"
            elif i % 3 == 0: res[i - 1] = "Fizz"
            elif i % 5 == 0: res[i - 1] = "Buzz"
        return res
