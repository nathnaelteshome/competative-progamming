from typing import List


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        can_cook = {s: True for s in supplies}  # r -> T/f
        recipe_map = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        res = []

        def dfs(r):
            if r in can_cook:
                return can_cook[r]

            can_cook[r] = False

            if r not in recipe_map:
                return False

            for ing in recipe_map[r]:
                if not dfs(ing):
                    return False

                can_cook[r] = True
                return can_cook[r]

        for index, r in enumerate(recipes):
            if dfs(r):
                res.append(r)

        return res


soln = Solution()
print(soln.findAllRecipes(["bread"], [["yeast", "flour"]], ["yeast"]))
