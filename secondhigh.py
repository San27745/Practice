def secondHighestOccurringElement(arr):
    cnt={}
    for i in arr:
        cnt[i]=cnt.get(i,0)+1

    f=sorted(set(cnt.values()),reverse=True)
    for i in arr:
        if cnt[i]==f[1]:
            return i
print(secondHighestOccurringElement([1,2,3,2,3,4,5,2]))