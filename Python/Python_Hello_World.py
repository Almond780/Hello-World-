#Hello world sub-processes

line = "-----------------------"

while(True):
    print(line)
    print("Press 'Q' to quit")
    print(line)
    print("Hello world!")
    choice = input("> ")
    if choice == "Q":
        break
    else:
        print("Please type 'Q'")
        
