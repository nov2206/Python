
# if and else

# age = 19

# if (age>18):
#     print(age,"adult")
# else:
#  print(age,"minor")

# #  else if



user_age = 23

age = int(input("enter your age "))

if age <= 12:
    category = "Child"
elif age <= 20:
    category = "Teenager"
elif age <= 30:
    category = "Young adult"
else:
    category = "Adult"

if(age == user_age):
        print(category,user_age,"match")
else:  
          print(category, "-", user_age, "age does not match")