def process(arr):
    for i in range(len(arr)):
        arr[i]=abs(arr[i])
        print(arr[i],end=' ')
        
n = int(input())
arr = list(map(int, input().split()))
process(arr)