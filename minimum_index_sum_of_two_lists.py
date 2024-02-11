class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dictionary1 = {value: index for index, value in enumerate(list1)}
        dictionary_ans = {}
        output = []

        for index, value in enumerate(list2):
            if value in dictionary1:
                dictionary_ans[value] = index + dictionary1[value]
        
        min_index = min(dictionary_ans.values())
                
        for value, sum_index in dictionary_ans.items():
            if sum_index == min_index:
                output.append(value)
                
        return output
        
        