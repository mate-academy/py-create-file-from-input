def main() -> None:
    filename = input("Enter name of the file: ")
    content = []
    while True:
        content_line = input(
            "Enter new line of content: "
        )
        if content_line == "stop":
            break
        content.append(content_line)
    with open(filename + ".txt", "w") as f:
        f.write("\n".join(content))


if __name__ == "__main__":
    main()
