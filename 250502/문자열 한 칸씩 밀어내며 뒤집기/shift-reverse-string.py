input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]
for query in queries:
    if query==1:
        input_str=input_str[1:]+input_str[0]
        print(input_str)
    elif query==2:
        input_str=input_str[len(input_str)-1]+input_str[:len(input_str)-1]
        print(input_str)
    elif query==3:
        input_str=list(input_str)
        input_str.reverse()
        input_str="".join(input_str)
        print(input_str)