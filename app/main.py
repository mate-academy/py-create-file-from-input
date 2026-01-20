def main() -> None:
    filename = input("Enter name of the file: ")
    file_content = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        file_content.append(line)

    with open(f"{filename}.txt", "w") as file:
        file.write("\n".join(file_content))


if __name__ == "__main__":
    main()
