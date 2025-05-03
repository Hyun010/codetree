def find(n):
    if n%2==0:
        p1=n//10
        p2=n%10
        if (p1+p2)%5==0:
            return "Yes"
    return "No"

n = int(input())
print(find(n))