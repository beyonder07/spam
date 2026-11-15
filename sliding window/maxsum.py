n=[2,5,1,8,2,9,1]
def max_sum_subarray(arr):
    sum=0
    i,j=0,0
    k=3
    max_sum=float('-inf')
    while j<len(arr):
        sum=sum+arr[j]
        if j-i+1<k:
            j+=1
        elif j-i+1==k:
            max_sum=max(max_sum,sum)
            sum-=arr[i]
            i+=1
            j+=1
    return max_sum
mx_sum=max_sum_subarray(n)
print(mx_sum)

