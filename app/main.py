def main() -> None:
    file_name = input("Enter name of the file: ")

    content = []
    while True:
        lines = input("Enter new line of content: ")
        if lines == "stop":
            break
        content.append(lines)

    with open(f"{file_name}.txt", "w") as f:
        f.write("\n".join(content))


if __name__ == "__main__":
    main()
