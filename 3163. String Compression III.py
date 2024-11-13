class Solution:
    def compressedString(self, word: str) -> str:
        # use Counter to find the reapetition of each character
        # loop through the word and make it a each char non repeating
        # for each key,val in Counter find the reminder = val % 9 and times = val // 9 
        #  {a:13, b:2} 
        i = 1
        ans = []
        
        while i < len(word):
            count = 1
            flag = False
            
            while i < len(word) and word[i] == word[i - 1]:
                count += 1
                i += 1
                flag = True


            reminder = count % 9
            times = count // 9
            print(i, reminder, times)

            for _ in range(times):
                ans.append(f"9{word[i - 1]}")

            if reminder and count > 1: ans.append((f"{reminder}{word[i - 1]}"))
            elif reminder: ans.append((f"{reminder}{word[i]}"))
            
            if flag: i -= 1
            i += 1

            

        return "".join(ans)

soln = Solution()
print(soln.compressedString("aaabcccd")) # 3a2b3cd
