x = 'om is a good boy and om is my best friend and om likes to play cricket om is a singer'

y = x.find('om')
print(y)

while y != -1:
    y = x.find('om', y+1)
    if y!=-1:
        print(y)