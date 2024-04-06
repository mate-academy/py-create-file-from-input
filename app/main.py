def main() -> None:
    name = input("Enter name of the file: ")
    content = []
    while True:
        new_record = input("Enter new line of content: ")
        if new_record == "stop":
            break
        content.append(new_record)
    with open(name + ".txt", "w") as file:
        for line in content:
            file.write(line)
            file.write("\n")


if __name__ == "__main__":
    main()
