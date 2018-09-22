class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack = [x] + self.stack
        self.min = min(self.stack)

    def pop(self):
        """
        :rtype: void
        """
        del self.stack[0]
        if self.stack != []: self.min = min(self.stack)
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min