txt = input()
ans = ""

for i in txt :
    if i.isupper():
        ans += i.lower()
    elif i.islower():
        ans += i.upper()
    else:
        ans += i

print(ans)