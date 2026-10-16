def highestOccurringElement(nums):
    cnt={}
    for i in nums:
       cnt[i]=cnt.get(i,0)+1
    max_cnt=max(cnt.values())
    for i in nums:
        if cnt[i]==max_cnt:
            return i
print(highestOccurringElement([1,2,3,3,2,4,2]))