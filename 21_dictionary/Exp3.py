x ={"Name":"Ritesh",
    "collage":"Global",
    "id":123456,
    "mail":"ritesh@gmail.com"
    }

print(x, id(x))

# y = x [1] # key error   
# y=x["Name"]    #we can call value from key

print(y)

x["Bus"]=True   # we can add a key value pair 

print(x, id(x))

x["Name"]= "Rajkumar"   # We can update a value
x["id"]=123457
x["mail"]="rajkumar@gmail.com"

print(x, id(x))

del x["Bus"]    # we can Delete a key-value pair

print(x, id (x))