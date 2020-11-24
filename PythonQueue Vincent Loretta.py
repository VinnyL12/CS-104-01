names = []
numberofnames = 0
for numberofnames in range (10):
    acceptedName = input("Please enter a name: ")
    names.append(acceptedName)
    numberofnames = numberofnames + 1
while len(names) > 0:
    print(names.pop(0))
    
