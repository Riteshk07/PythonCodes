marks={}
s= int(input("How many Student in the Class? "))

n= int(input("How many Subject in Your Course? "))
for k in range(s):
    studentName= input("Enter Student's name: ")
    for i in range(1,n+1):
        subName=input(f"Enter Subject {i} Name: ")
        mMarks= eval(input(f"Enter subject {i} marks: "))
        while mMarks>100:
            print("Please! Enter Correct Marks")
            mMarks= int (input(f"Enter subject {i} marks: "))
        marks[subName]= mMarks

    print(f"\t\tABCD Board\n\tABC Higher Secondary School\nStudent's Name: {studentName}")
    # print(marks)
    for x,y in marks.items():
        print(f"\t{x} --> {y}")
    avg=round(sum(marks.values())/n,2)
    print(f"\t\tTotal Marks: {sum(marks.values())}")
    # print(f'The percentage of this Student is: {avg} %' )

    if (avg<33):
        print(f"you are fail deu to total percentage less than 33\nYour total percentage is: {avg} %")
    elif (avg<=40):
        print(f"Congratulations...\nYou are pass with Grade D\nYour total percentage is: {avg} %")
    elif (avg<=50):
        print(f"Congratulations...\nYou are pass with Grade C2\nYour total percentage is: {avg} %")
    elif (avg<=60):
        print(f"Congratulations...\nYou are pass with Grade C1\nYour total percentage is: {avg} %")
    elif (avg<=70):
        print(f"Congratulations...\nYou are pass with Grade B2\nYour total percentage is: {avg} %")
    elif (avg<=80):
        print(f"Congratulations...\nYou are pass with Grade B1\nYour total percentage is: {avg} %")
    elif (avg<=90):
        print(f"Congratulations...\nYou are pass with Grade A2\nYour total percentage is: {avg} %")
    else:
        print(f"Congratulations...\nYou are pass with Grade A1\nYour total percentage is: {avg} %")