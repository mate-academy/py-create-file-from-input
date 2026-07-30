def main() -> None:
    name = str(input("Enter name of the file: "))
    name1 = f"{name}.txt"
    new = ""
    while True:
        file_content = str(input("Enter new line of content: "))
        if file_content == "stop":
            break
        new += file_content + "\n"
    with open(name1, "a") as doc:
        doc.write(new)


if __name__ == "__main__":
    main()
