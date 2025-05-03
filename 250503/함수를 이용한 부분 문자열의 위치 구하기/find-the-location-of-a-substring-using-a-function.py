def find(s1,s2):
    try:
        i=s1.index(s2)
        return i
    except:
        return -1

text = input()
pattern = input()
print(find(text,pattern))