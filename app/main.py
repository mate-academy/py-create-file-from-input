def app_for_creation_files():
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "a") as file:
        while True:
            line_of_content = input("Enter new line of content: ")
            if line_of_content == "stop":
                break
            file.write(f"{line_of_content}\n")


app_for_creation_files()
