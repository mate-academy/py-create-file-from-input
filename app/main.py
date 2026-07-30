def main() -> None:
    filename = input("Enter name of the file: ")

    lst = []
    content = ""
    while content != "stop":
        content = input("Enter new line of content: ")
        if content != "stop":
            lst.append(content)

    with open(f"{filename}.txt", "a") as f:
        for line in lst:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
