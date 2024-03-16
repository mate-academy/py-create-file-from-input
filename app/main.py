def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    file_name += ".txt"

    with open(file_name, "a") as file:
        for line in content:
            file.write(line + "\n")

    print(f'# File name: "{file_name}"')
    print("# File content:")
    for line in content:
        print(f"# {line}")


if __name__ == "__main__":
    main()