from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        h, w = len(image), len(image[0])

        def dfs(r,c,src_color):
            # return for invalid coordinates, repeated traversal or different color
            if (r < 0 or c < 0 or r >= h or c >= w or
                image[r][c] == color or
                image[r][c] != src_color):
                return

            image[r][c] = color

            dfs(r-1, c, src_color)
            dfs(r+1, c, src_color)
            dfs(r, c-1, src_color)
            dfs(r, c+1, src_color)

        dfs(sr,sc, src_color=image[sr][sc])

        return image