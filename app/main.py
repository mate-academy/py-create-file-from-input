def main():
    file_name = input("Enter name of the file: ") + ".txt"

    with open(file_name, "w") as file:
        value = True
        while value:
            content = input("Enter new line of content: ")
            if content == "stop":
                value = False
            else:
                file.write(content + "\n")


if __name__ == "__main__":
    main()