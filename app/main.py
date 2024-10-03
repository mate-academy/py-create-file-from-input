file_name = input("Enter name of the file: ")

while True:
    file_content = input("Enter new line of content: ")
    if file_content == "stop":
        break

    with open(f"{file_name}", "a") as f:
        f.write(f"{file_content}\n")
