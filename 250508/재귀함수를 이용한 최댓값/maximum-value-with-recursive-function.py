def p(arr):
    global target
    if arr==[]:
        return target
    t=arr.pop()
    if target<t:
        target=t
    return p(arr)

n = int(input())
arr = list(map(int, input().split()))
target=-1
print(p(arr))