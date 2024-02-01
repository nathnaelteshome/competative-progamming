class Solution:
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        l = 0
        i = 0
        minn = collections.deque()
        maxx = collections.deque()
        res = 0
        while i < len(nums):
            while maxx and nums[i] >= nums[maxx[-1]]:
                maxx.pop()
            while minn and nums[i] <= nums[minn[-1]]:
                minn.pop()
            maxx.append(i)
            minn.append(i)

            if nums[maxx[0]]-nums[minn[0]] <= limit:
                res = max(res, maxx[0]-minn[0])

            if nums[maxx[0]]-nums[minn[0]] > limit:
                l += 1
                if(l > maxx[0]):
                    maxx.popleft()

                if(l > minn[0]):
                    minn.popleft()
            else:
                res = max(res, i-l+1)
                i += 1
        return res
