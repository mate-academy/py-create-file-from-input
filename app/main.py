def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = file_name + ".txt"

    content = []
    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        content.append(text)

    file_to_write = open(file_name, "w")

    for line in content:
        file_to_write.write(f"{line}\n")

    file_to_write.close()


if __name__ == "__main__":
    main()
