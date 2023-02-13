class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                continue
            if s[i] == ']':
                currStr = ''
                while stack:
                    currChar = stack.pop()
                    if currChar == '[':
                        count = 0
                        power = 1
                        while stack:
                            n = stack.pop()
                            if not n.isnumeric():
                                stack.append(n)
                                break
                            count += int(n)*power
                            power *= 10
                        currStr *= count
                        stack.extend([c for c in currStr])
                        break
                    currStr = currChar + currStr
            else:
                stack.append(s[i])

        return ''.join(stack)
