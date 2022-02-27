x=int(input("Enter books Price: "))

result= "All Books dede Bhai" if x<=0 else("Buy Now" if x<=200 else("Buy Later" if x<=400 else "Don't Buy" ))
# result = "Buy Now" if x <= 200 else ("Buy Later" if x > 200 and x <=400 else "Don't Buy")
# result = "Buy Now" if x <= 200 else ("Buy Later" if x <= 400 else "Don't Buy")
# result = "Buy Now" if x <= 200 else ("Don't Buy" if x > 400 else "Buy Later")

print(result)
