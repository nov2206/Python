''' Tuple bhi list ki tarah multiple values store karta hai, 
lekin tuple ko create karne ke baad uske elements change 
 nahi kar sakte.'''


# student = ("Deep","Disha","Dev", "Delhi")

# print(student.count("D"))
# print(student.index("Delhi"))
# print(student[1])


# if access the tuple we use
# Remember:
# - Indexing starts from 0.
# - student[0] means first element.
# - student[1] means second element.


# we have learn negative indexing

# print(student[2:4])



student = (10,20,30,40,50)
i = 0 

while i < len(student):
    print(student[i])
    i+=1