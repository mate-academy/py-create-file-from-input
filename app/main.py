def main() -> str:
    file_name = input("Enter name of the file: ")
    content = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    file_content = "\n".join(content)

    file_name_with_extension = f"{file_name}.txt"

    with open(file_name_with_extension, "w") as file:
        file.write(file_content)

    print(f'File name: "{file_name_with_extension}"\nFile content:'
          f"\n{file_content}")


if __name__ == "__main__":
    main()
