n=[]
count=int(input("Enter how many number in the list: "))
for i in range(count):
    r=int(input("Enter number: "))
    n.append(r)
sum=0
for num in n:
    if num%2==0:
        sum+=num
print(sum)



