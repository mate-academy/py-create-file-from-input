name = input("Enter file name: ")
with open(f"{name}.txt", "a") as f:
    user_string = 1
    while user_string != "stop":
        user_string = input("Enter string to add: ")
        if user_string != "stop":
            f.write(f"{user_string}\n")
