# parrot_while.py

message = ""
while message != "exit":
    message = input("Tell me something and i will repeat it back to you : ")
    # print("Enter exit to quit")
    if message != "exit":
        print(message)
        print("Enter exit to quit")
