class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        l = path.split('/')
        res = []
        for val in l:
            if val != '' and val != '.':
                if val == '..' and res != []: res.pop()
                elif val == '..': pass
                else: res.append(val)
        return '/' + '/'.join(res)
