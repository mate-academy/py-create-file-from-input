def main() -> None:
    filename = input("Enter name of the file: ")

    content = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)

    with open(f"{filename}.txt", "w") as file:
        file.write("\n".join(content))

    print(f"File name: \'{filename}.txt\'")
    print("File content: ")
    for line in content:
        print(line)


if __name__ == "__main__":
    main()
