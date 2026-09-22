def main() -> None:
    file_basename = input("Enter name of the file: ")

    content = []

    while True:
        line = input("Enter new line of content: ")

        if line == "stop":
            break

        content.append(line)

    filename = f"{file_basename}.txt"

    with open(filename, "w") as file:
        for line in content:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
