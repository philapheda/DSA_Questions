class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        ans = []
        for i in image:
            i.reverse()
        for j in image:
            ans2 = []
            for k in j:
                if k == 1:
                    k -=1
                    ans2.append(k)
                else:
                    k += 1
                    ans2.append(k)
            ans.append(ans2)
        return(ans)
        