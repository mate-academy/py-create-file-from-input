def main() -> None:
    filename = input("Enter name of the file: ")
    filename = filename + ".txt"
    userinput = list()
    while True:
        newline = input("Enter new line of content: ")
        if newline != "stop":
            userinput += newline + "\n"
        else:
            break
    with open(filename, "a") as file:
        file.writelines(userinput)


if __name__ == "__main__":
    main()
