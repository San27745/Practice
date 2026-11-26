def sumOfFrequencies(arr):
    cnt={}
    for i in arr:
        cnt[i]=cnt.get(i,0)+1
    return max(cnt.values())+min(cnt.values())
print(sumOfFrequencies([1,2,3,4,4,3,2,3]))