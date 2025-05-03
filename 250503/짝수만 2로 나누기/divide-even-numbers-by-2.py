def half_only(arr):
    for i in arr:
        if i%2==0:
            print(i//2,end=' ')
        else:
            print(i,end=' ')

n = int(input())
arr = list(map(int, input().split()))
half_only(arr)