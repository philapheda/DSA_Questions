class Solution:
    def sortSentence(self, s: str) -> str:
        ans = list(map(str, s.split()))
        arr = []
        for index, i in enumerate(ans):
            arr.append(i[-1])
            ans[index] = i.replace(i[-1], "")
        for i in range(len(arr)):
            for j in range(len(arr) - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    ans[j], ans[j + 1] = ans[j + 1], ans[j] 
        return " ".join(ans)