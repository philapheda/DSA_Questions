class Solution:
    def similarPairs(self, words: list[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if sorted(set(words[i])) == sorted(set(words[j])):
                    count+=1
        return count