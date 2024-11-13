class Solution:
    def makeFancyString(self, parcel_weights: list) -> int:
        l = 0 
        r = len(parcel_weights) - 1
        p = sorted(parcel_weights)
        ans = 0
        chosen = set()
        while l <= r:
            if l == r:
                if parcel_weights[l] not in chosen:
                    ans += parcel_weights[l]
                l += 1
                r -= 1
                continue
            inners = [parcel_weights[l+1],parcel_weights[r-1]]
            outers = [parcel_weights[l],parcel_weights[r]]
            temp = inners + outers
            i = 0
            while i < len(temp):
                if temp[i] in chosen:
                    temp.pop(i)
                else:
                    i += 1
            if not temp:
                while p:
                  t = p.pop()
                  if t not in chosen:
                      ans += t
                      chosen.add(t)
                      break
                l += 1
                r -= 1
                continue
            elif len(temp) == 1:
                ans += temp[0]
                chosen.add(temp[0])
                l += 1
                r -= 1
                continue
            s = sorted(temp,reverse=True)[:2]
            if s == sorted(outers):
                s = [max(outers),max(inners)]
            if s[0] in inners:
                s[0],s[1] = s[1],s[0]
            
            ans += s[0]
            chosen.add(s[0])
            l += 1
            r -= 1

        return ans


soln = Solution()

print(soln.makeFancyString([4,4,8,5,3,2])) # 17
print(soln.makeFancyString([2,1,8,5,6,2,4])) # 7
print(soln.makeFancyString([5,7,2,13,6])) # 7
print(soln.makeFancyString([4,4,4,4,4,4,4,4,4,4,6,7,2,8,10,11,12,13,3,4,4,4,4,4,4,4,4,4,4,4,4,4])) # 9