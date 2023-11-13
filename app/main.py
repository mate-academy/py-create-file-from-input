def main() -> None:
    file_name = input("Enter name of the file: ")
    content = ""

    while True:
        new_line = input("Enter new line of content: ") + "\n"

        if "stop" in new_line:
            break
        else:
            content += new_line

    with open(f"{file_name}.txt", "w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
