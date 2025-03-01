from typing import List


class Solution:
    def removeSubfolders(self, folder) -> list[str]:
        folder.sort()

        result = [folder[0]]

        for i, fold in enumerate(folder[1:]):
            lastFolder = result[-1]
            lastFolder += "/"

            # check if the current folder starts with the last added folder path
            if not folder[i].startswith(lastFolder):
                result.append(folder[i])

        return result


soln = Solution()
soln.removeSubfolders(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])
