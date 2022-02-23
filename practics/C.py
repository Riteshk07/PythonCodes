mMarks= eval(input("Enter subject  marks: "))
# print(mMarks,type(mMarks))

while type(mMarks)==str:
    print("Please! Enter Correct Marks")
    mMarks= eval(input(f"Enter subject  marks: "))
while mMarks>100:
    print("Please! Enter Correct Marks")
    mMarks= eval (input(f"Enter subject  marks: "))
print("your num is ", mMarks )  