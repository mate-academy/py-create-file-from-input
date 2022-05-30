file_name = input("Enter name of the file: ") + ".txt"
with open(file_name, 'a') as file:
    while True:    # will stop when user enters "stop"
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        file.write(line + "\n")
