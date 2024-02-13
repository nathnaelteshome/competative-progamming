class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_distance = abs(target[0]) + abs(target[1])
        can_escape = True

        for ghost in ghosts:
            x = abs(ghost[0] - target[0])
            y = abs(ghost[1] - target[1])
            ghost_distance = x + y
            
            if ghost_distance <= my_distance:
                can_escape = False
        
        return can_escape
