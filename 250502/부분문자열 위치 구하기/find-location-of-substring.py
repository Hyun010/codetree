input_str = input()
target_str = input()
for i in range(len(input_str)-len(target_str)):
    if input_str[i:i+len(target_str)]==target_str:
        print(i)
        break
else:
    print(-1)