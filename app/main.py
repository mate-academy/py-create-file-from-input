def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    lst = []
    text = ""

    while text != "stop":
        text = input("Enter new line of content: ")
        if text != "stop":
            lst.append(text)

    with open(file_name, "a") as file:
        for line in lst:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
