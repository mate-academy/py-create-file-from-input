def main():
    file_name = input("Enter name of the file: ")
    message = ""
    text = []

    while message != "stop":
        message = input("Enter new line of content: ")
        if message != "stop":
            text.append(message + "\n")

    with open(file_name + ".txt", "w") as file:
        file.writelines(text)


if __name__ == "__main__":
    main()
