def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    file_content = "\n".join(content)

    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)

    print(f"File '{file_name}.txt' created successfully.")


if __name__ == "__main__":
    main()
