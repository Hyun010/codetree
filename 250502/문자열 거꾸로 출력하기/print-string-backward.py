while True:
    s=list(input())
    if s==["E","N","D"]:
        break
    s.reverse()
    print("".join(s))