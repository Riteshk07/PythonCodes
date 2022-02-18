letter='''Dear <|NAME|>,
Greeting from ISRDC Jabalpur. I am happy to tell you about your selection
You are selected!
Have a great day ahead
Date: <|DATE|> '''

name=input("Enter your Name\n")
date=input("Enter Date\n")
letter=letter.replace("<|NAME|>", name)
letter=letter.replace("<|DATE|>", date)
print(letter)