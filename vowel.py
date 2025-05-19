n=input().lower()
count=0
vow=""
for i in range(len(n)):
    if n[i] in "aeiou":
        count+=1
        vow+=n[i]
print(f"{count},({vow})")