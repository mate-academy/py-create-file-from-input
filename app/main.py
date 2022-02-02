def file_creating():

    file_name = input("Enter name of the file: ")

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        with open(file_name + ".txt", "a") as file:
            file.write(line + "\n")


if __name__ == "__main__":
    file_creating()
