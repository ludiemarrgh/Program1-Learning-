# Write  a program to repaeat entries of 10 students with thier grades the print them out 
# variables
Student = str(input("Enter student's name: "))
math = int(input("Enter student's grade for math:"))
science = int(input("Enter student's grade for science:"))
english = int(input("Enter student's grade for english:"))

print("Student:", Student)

#Subjects 
# math
if math >= 90 and math <= 100:
    print("A", math)
elif math >= 70 and math < 90:
    print("B", math)
elif math >= 50 and math < 70:
    print("C", math) 
elif math >= 30 and math < 50:
    print("D", math)
else:
    print("E", math)    
# Science
    
if science >= 90 and science <= 100:
    print("A", science)
elif science >= 70 and science < 90:
    print("B", science)
elif science >= 50 and science < 70:
    print("C", science) 
elif science >= 30 and science < 50:
    print("D", science)
else:
    print("E", science) 
#English

if english >= 90 and english <= 100:
    print("A", english)
elif english >= 70 and english < 90:
    print("B", english)
elif english >= 50 and english < 70:
    print("C", english) 
elif english >= 30 and english < 50:
    print("D", english)
else:
    print("E", english)
average = (math + english + science)/3
print("Average:", average)