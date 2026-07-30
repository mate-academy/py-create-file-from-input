def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    with open(filename, "w") as file:
        content = ""
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            content += line + "\n"
        file.write(content)


if __name__ == "__main__":
    main()
