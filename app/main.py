def main() -> None:
    name = input("Enter name of the file: ")
    content_lines = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        content_lines.append(new_line)

    with open(f"{name}.txt", "w") as f:
        f.write("\n".join(content_lines))


if __name__ == "__main__":
    main()
