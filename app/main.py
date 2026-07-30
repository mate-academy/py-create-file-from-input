def main():
    name1 = input("Enter name of the file: ")
    value = ""
    with open(name1 + '.txt', "a") as file:
        while value != "stop":
            value = input("Enter new line of content: ")
            if value != "stop":
                file.write(value + "\n")


if __name__ == "__main__":
    main()
