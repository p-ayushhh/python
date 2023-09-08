num = int(input("enter a number"))
if num<0:
    print("pls enter a valid a number ")
else:
        fact = 1
        while num>0:
            fact *=num
            num -=1
        print("the fact is ",fact)
