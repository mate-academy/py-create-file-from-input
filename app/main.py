def main() -> None:
    name = input("Enter name of the file: ")
    content = ""

    while (True):
        new_line = input("Enter new line of content: ")
        if new_line != "stop":
            content += new_line + "\n"
        else:
            break

    with open(f"{name}.txt", "w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
