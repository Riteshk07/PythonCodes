x= {}

x["Name"]= "Ritesh"

x["Friends"]=[]
x["Friends"].append(input("Enter Friend Name:\n"))
x["Friends"].append(input("Enter Friend Name:\n"))
x["Friends"].append(input("Enter Friend Name:\n"))

a=input("enter city: ")
b=input("enter city: ")
c=input("enter city: ")
x["City"]=(a, b, c)

print(x)

print(f'{x["Friends"][0]} lives in {x["City"][0]}')
print(f'{x["Friends"][1]} lives in {x["City"][1]}')
print(f'{x["Friends"][2]} lives in {x["City"][2]}')