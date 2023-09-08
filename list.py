
# creating a list of number
numbers = [1,2,3,4,5,]
# accessing elements in a list
print(numbers [0])
print(numbers [2])
# modifying elements in a list
numbers [1] = 10
print(numbers)
#concatenating lists
fruits1 = ["apple", "banana"]
fruits2 = ["orange", "graph"]
all_fruits = fruits1 + fruits2
print(all_fruits)
# appending and extending a list
fruits1 . append("pear")
fruits2 . extend (["kiwi","pineapple"])
print(fruits1)
print(fruits2)
#new p
numbers = [1,2,3,4,5,]
#using a for loop to iterate through the list
for num in numbers:
  print(num)
#using list comprehension to create a new list
squared_numbers=[num ** 2 for num in numbers]
print(squared_numbers)
# sorting a list
numbers =  [3,1,4,1,5,9,2]
# Sorting a list
numbers = [3,1,4,1,5,9,2]
numbers.sort()
print(numbers)
# Finding index of an element
index = numbers.index(4)
print(index)
# Reversing a list 
numbers.reverse()
print(numbers)




