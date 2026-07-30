def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)

    with open(f"{file_name}.txt", "w") as file:
        file.write("\n".join(content))

    print(f"File '{file_name}.txt' created successfully!")


if __name__ == "__main__":
    main()
