def numberOfSubarrays(self, nums, k):
    def max(k):
        answer = 0
        index1 = 0
        for index2 in range(len(nums)):
            k -= nums[index2] % 2
            while k < 0:
                k += nums[index1] % 2
                index1 += 1
            answer += index2 - index1 + 1
        return answer

    return max(k) - max(k - 1)
