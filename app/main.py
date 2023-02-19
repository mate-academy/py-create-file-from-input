def main() -> str:
    filename = input("Enter name of the file: ")
    content = ""

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content += line + "\n"

    with open(filename + ".txt", "w") as file:
        file.write(content)

    print(f"File name: {filename}.txt")
    print("File content:")
    print(content)


if __name__ == "__main__":
    main()
