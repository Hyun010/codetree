n = int(input())
points = [(int(i+1), list(map(int, input().split()))) for i in range(n)]
points.sort(key=lambda x: (abs(x[1][0])+abs(x[1][1]),x[0]))
for k in points:
    print(k[0])