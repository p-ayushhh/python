#5
num = int (input ("enter a number "))
if num<0:
  print("pls enter a valid number")
else:
    sum = 0;
    while num>0:
      sum+= num
      num -= 1
    print("the sum is",sum)
