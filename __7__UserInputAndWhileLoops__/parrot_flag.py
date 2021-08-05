# parrot_flag.py

active = True
message = ""
while active:
    message = input("Tell me something and i will repeat it back to you : ")
    if message == "exit":
        active = False
    else:
        print(message)
        print("Enter exit to quit")