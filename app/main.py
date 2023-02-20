def main():
    file_name = input("Enter name of the file: ")

    content = []
    txt = ""

    while txt != "stop":
        txt = input("Enter new line of content: ")
        if txt != "stop":
            content.append(txt)

    with open(f"{file_name}.txt", "a") as file:
        for line in content:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
