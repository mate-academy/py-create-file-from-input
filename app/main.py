file_name = input("Enter file name: ")
with open(f"{file_name}.txt", "a") as f:
    user_string = ""
    while user_string != "stop":
        user_string = input("Enter string to add: ")
        if user_string != "stop":
            f.write(f"{user_string}\n")
