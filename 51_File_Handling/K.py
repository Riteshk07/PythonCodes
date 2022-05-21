with open("Words.txt", "r") as Rfile :
    x = Rfile.readlines()
    ch=0
    row=0
    word=0
    for i in x :
        print(i, end="")
        for j in i :
            if (j==" " or j=="\n"):
                word+=1
        ch+=len(i)
        row+=1
    print()
    print("number of words: ",word)
    print("Number of Rows: ", row)
    print("Number of Charecter: ", ch)
