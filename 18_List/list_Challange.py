markList=[]
markList.append(float(input("Enter Marks of Hindi\n")))
markList.append(float(input("Enter Marks of English \n")))
markList.append(float(input("Enter Marks of Science \n")))
markList.append(float(input("Enter Marks of Social Science\n")))
markList.append(float(input("Enter Marks of Math \n")))
markList.append(float(input("Enter Marks of Sanskrit\n")))

print(markList)
avg=round(sum(markList)/6,2)
print(f"Total Marks: {sum(markList)}")
print(f'The percentage of this Student is: {avg} %' )

markList[1]=float(input('Update index 1 subject of marks\n'))
markList[2]=float(input('Update index 2 subject of marks\n'))

print(markList)
avg=round(sum(markList)/6,2)
print(f"Total Marks: {sum(markList)}")
print(f'The percentage of this Student is: {avg} %' )
