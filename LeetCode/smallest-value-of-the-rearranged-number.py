class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = {}
        neg = False
        ans = ""
        if len(set(str(num))) == 1:
            return num
        for i in str(num):
            if i == '-':
                neg = True
                continue
            nums[int(i)] = nums.get(int(i), 0)+1
        if not neg:
            ans = ""
            done = False
            sorted_nums = dict(sorted(nums.items()))
            while len(ans)!=len(str(num)):
                if not ans:
                    for i in sorted_nums:
                        if i == 0:
                            continue
                        else:
                            ans+=str(i)
                            sorted_nums[i] = sorted_nums.get(i)-1
                            break
                else:
                    for i in sorted_nums:
                        ans+=str(i)*sorted_nums[i]
            return int(ans)
        else:
            sorted_nums = dict(sorted(nums.items(), reverse = True))
            ans=""
            while len(ans)!=len(str(num))-1:
                for i in sorted_nums:
                    ans+=str(i)*sorted_nums[i]
            return -int(ans)
        