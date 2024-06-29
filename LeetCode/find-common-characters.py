class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        words_dic = []
        ans = []
        for i in words:
            word_dic = {}
            for j in range(len(i)):
                word_dic[i[j]] = word_dic.get(i[j],0)+1
            words_dic.append(word_dic)
        for k in words_dic[0]:
            min_num = words_dic[0].get(k)
            found =  True
            for j in words_dic:
                if k not in j:
                    found = False
            if found:
                for j in words_dic:
                    if k in j:
                        min_num = min(min_num, j[k])
                for i in range(min_num):
                    ans.append(k)
        return ans
                