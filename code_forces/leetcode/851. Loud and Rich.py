def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
    ans = [[float("inf"), 0]] * len(quiet)
    adj = collections.defaultdict(list)
    for a, b in richer:
        adj[b].append(a)

    def dfs(node):
        if ans[node][0] != float("inf"):
            return ans[node]
        ans[node] = [quiet[node], node]

        for rich_Nei in adj[node]:
            k = dfs(rich_Nei)
            if k[0] < ans[node][0]:
                ans[node] = k

        return ans[node]

    for node in range(len(quiet)):
        if ans[node][0] == float("inf"):
            dfs(node)

    return [i[1] for i in ans]


# input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
# Output: [5,5,2,5,4,5,6,7]
