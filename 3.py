n = str(input())
if len(n) == 5:
    print(int(n[::-1]))
else:
    print(int(n[0]+n[:-6:-1]))
