#Python Hello world Launcher
#The elif's are messy

import subprocess

line = "-----------------------" # change the length if you want
vinput = "Invalid input"

while(True):
    print(line)
    print("---Hello World Luancher---")
    print(line)
    print("Press 'Q' to quit")
    print(line)
    print("Avalible Tools")
    print("1. Python")
    print("2. C++")
    print("3. C")
    print("4. Javascript/CSS/HTML")
    print("5. x86-64 intel(TM) syntax Assembly")
    # Add more of Avalible Tools
    choice = input("> ")
    if choice == "Q":
        break
    elif choice == "1":
        subprocess.run(["python3", "/home/user/Python/Python_Hello_World.py"])
        # #Change your absolute path 
    elif choice == "2":
        # Run a compiled executable
        subprocess.run(["/home/user/C++/executable"]) 
        # #Change your absolute path 
    elif choice == "3":
        # Run a compiled executable
        subprocess.run(["/home/user/C/executable"]) 
        # #Change your absolute path 
    
    else:
        print(vinput)
