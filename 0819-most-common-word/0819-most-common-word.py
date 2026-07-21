from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")
        words = paragraph.lower().split()
        count = Counter(word for word in words if word not in banned)
        return max(count, key=count.get)