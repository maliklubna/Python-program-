num=253
temp=num
r=num%10
rev=0
rev=rev*10+r
num=num//10
r=num%10
rev=rev*10+r
num=num//10
r=num%10
rev=rev*10+r
print(f"reverse of {temp} is, {rev}")