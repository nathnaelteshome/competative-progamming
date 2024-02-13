class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        different_pairs = set(fronts + backs)

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                different_pairs.discard(fronts[i])

        if different_pairs:
            return min(different_pairs)
        return 0

        