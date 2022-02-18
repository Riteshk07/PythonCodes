import time
name= "Ritesh"
string=f"Good Morning...\n\tMy name is {name}, \n\t\tHave a Good Day... :) "
for i in string:
    print(i, end="", flush= True)
    time.sleep(0.1)
