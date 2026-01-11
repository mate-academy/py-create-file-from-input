def main() -> None:
    filename = input("Enter name of the file: ")
    filename += ".txt"
    content = []
    while True:
        string = input("Enter new line of content: ")
        if string == "stop":
            break
        else:
            content.append(string + "\n")

    with open(filename, "a") as f:
        for string in content:
            f.write(string)


if __name__ == "__main__":
    main()
