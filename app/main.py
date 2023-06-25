def main() -> None:
    file_name = input("Enter name of the file: ")

    content= []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    file_path: str = file_name + ".txt"
    with open(file_path, "w") as file:
        file.write("\n".join(content))

    print(f"File name: {file_path}")
    print("File content:")
    for line in content:
        print(line)


if __name__ == "__main__":
    main()
