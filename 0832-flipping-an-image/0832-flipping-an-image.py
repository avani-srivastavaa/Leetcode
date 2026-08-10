class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flipped = []

        for i in range(len(image)):
            flipped.append(image[i][::-1])

        for i in range(len(flipped)):
            for j in range(len(flipped[i])):
                if flipped[i][j] == 0:
                    flipped[i][j] = 1
                else:
                    flipped[i][j] = 0

        return flipped