def main() -> None:
    filename = input("Enter name of the file: ")
    ls = []

    while True:
        content_line = input("Enter new line of content: ")
        if content_line == "stop":
            break
        ls.append(content_line)

    with open(f"{filename}.txt", "w") as f:
        for content_line in ls:
            f.write(content_line + "\n")


if __name__ == "__main__":
    main()
