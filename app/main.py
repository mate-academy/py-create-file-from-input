def main() -> None:
    filename = input("Enter name of the file: ")

    content = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)

    with open(f"{filename}.txt", "w") as f:
        for line in content:
            f.write(line + "\n")

    print(f'File "{filename}" has been created with the provided content.')


if __name__ == "__main__":
    main()
