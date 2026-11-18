def main() -> None:
    file_basename = input("Enter name of the file: ")

    content = []
    while True:
        line = input("Enter new line of content: ")

        if line == "stop":
            break

        content.append(line)

    with open(f"{file_basename}.txt", "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
