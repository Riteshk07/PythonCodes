x = input("Enter Purse Value(in number): ")

saving = int(x) if x.isdigit() else ""

if type(saving)==str or saving<10 :
    print("\u0924\u0941\u092E\u0938\u0947 \u0928\u093E \u0939\u094B \u092A\u093E\u092F\u0947\u0917\u093E,\nDating tumhare bas ki nahi hai")
elif saving>5000:
	if saving>10000:
		print("Roadtrip with\n")
	else :
		print( "shoping with\n")

	print("F.R.I.D.A.Y." )
elif saving>2000:
	if saving>4000:
		print( "Shoping with\n")
	else:
		print( "Watch movie with \n")

	print("Siri" )
else:
	if saving>1000:
		print( "I will go to watch movie with\n")
	else:
		print( "Go to park with\n")

	print( "Rajkumar")

