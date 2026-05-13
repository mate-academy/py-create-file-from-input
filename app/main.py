def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []

    stop = True
    while stop:
        line = input("Enter new line of content: ")
        if line == "stop":
            stop = False
        else:
            content.append(line)

    open(f"{file_name}.txt", "w").write("\n".join(content))


if __name__ == "__main__":
    main()
