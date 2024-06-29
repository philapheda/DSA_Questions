class Solution:
    def freqAlphabets(self, s: str) -> str:
        i=0
        done = False
        soln = ""
        alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        while i<len(s):
            try:
                if s[i+2] == "#":
                    num = int(s[i]+s[i+1])
                    soln+=alp[num-1]
                    done = True
                else:
                    add = list(s[i:i+1])
                    for j in add:
                        soln += alp[int(j)-1]
            except IndexError:
                add = list(s[i:i+1])
                for j in add:
                    soln += alp[int(j)-1]
            if done:
                i+=3
                done = False
            else:
                i+=1
        return soln