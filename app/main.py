def main() -> None:
    name = input("Enter name of the file: ")
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)
    with open(f"{name}.txt", "w") as f:
        for line in content:
            f.write(line + "\n")
    print(f"File name: '{name}.txt'")
    print("File content:")
    for line in content:
        print(line)


if __name__ == "__main__":
    main()
