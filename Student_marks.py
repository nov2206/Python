#  student marks 


name = input("Name the student");
age = int(input("enter your age "));
hindi = int(input("enter your hindi "));
english = int(input("enter your english "));
math = int(input("enter your math "));
science =int(input("enter your science "));
sst = int(input("enter your sst "));

total = hindi+english+math+science+sst
percent = total/500*100

print(f" name is {name} age is {age}")
print(f"total is {total} ")
print (percent)
