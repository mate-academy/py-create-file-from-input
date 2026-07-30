def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(f"{line}\n")

    with open(f"{file_name}.txt", "w") as f:
        f.writelines(content)


if __name__ == "__main__":
    main()
