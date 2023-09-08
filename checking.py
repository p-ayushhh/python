
my_dict = {"city" :"20", "ayush" :"6", "cse":"8","name":"ayush prajapati"}
print(my_dict["ayush"])
# removing a key - value pair
del my_dict["city"]
print(my_dict)


#checking if a key exists in the dictionary
if "name" in my_dict:
    print("name:", my_dict["name"])

#getting all key and values

keys = my_dict.keys()
value = my_dict . values()

#iterating through keys and values

for key , value in my_dict . items():
    print(key,":",value)







            

