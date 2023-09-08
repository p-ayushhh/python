#creating a dictionary of user Information:
user ={
    "username": "ayush",
    "full_name": "prajapati",
    "email": "ayushkrprajapati@gmail.com",
    "age":"90",
    "game":"cricket",
    "skills":"c,html,css,java,java script,python,nodejs,github,leet code,",
    "city":"chaibasa",
    "dream city":"kedarnath",
    "intrested":"graffic designing,editng",
    "favourite movie": "fast and ferious,herry porter",
    "phone number":"6370094797",
    }
print(user["full_name"])
print(user["username"])
print(user["email"])
print(user["game"])
print(user["skills"])
print(user["city"])
print(user["dream city"])
print(user["intrested"])
print(user["favourite movie"])
print(user.get("phone number","phone number not specified"))
print(user.get("age","age not specified"))

"""
deffination of sets:-
In python, a set is a built-in data type that represents an unorderd collection of unique element.sets are
useful when you want to store and you don't need to maintain aspecfic order of the elements.
"""


s1={1,2,3,4,5,6}
s2={5,1,7,4,8}
s3=s1.union(s2)
print(s3)
print(s1|s2)
