english=int(input("enter marks in english\n"))
maths=int(input("enter marks in maths\n"))
sc=int(input("enter marks in sc\n"))
ssc=int(input("enter marks in ssc\n"))
urdu=int(input("enter marks in urdu\n"))
total=english+maths+sc+ssc+urdu
per=total/500*100
if per>=75:
    print("distingsion");
elif per>=60:
     print("1st div") ;  
elif per>=50:
     print("2nd div");
elif per>= 40:
     print(" 3rd div");
else :
     print("fail");