#Python Hello world Launcher

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
    elif choice == "4":
        # Run a compiled executable
        subprocess.run(["/home/user/Java/executable"]) 
        # #Change your absolute path 
    elif choice == "5":
        # Run a compiled executable
        subprocess.run(["/home/user/Javascript/executable"]) 
        # #Change your absolute path 
    elif choice == "6":
        # Run a compiled executable
        subprocess.run(["/home/user/Rust/executable"]) 
        # #Change your absolute path 
    elif choice == "7":
        # Run a compiled executable
        subprocess.run(["/home/user/HTML/executable"]) 
        # #Change your absolute path 
    elif choice == "8":
        # Run a compiled executable
        subprocess.run(["/home/user/brainf*ck/executable"]) 
        # #Change your absolute path 
    elif choice == "10":
        # Run a compiled executable
        subprocess.run(["/home/user/x86_aseembly/executable"]) 
        # #Change your absolute path 
    else:
        print(vinput)
