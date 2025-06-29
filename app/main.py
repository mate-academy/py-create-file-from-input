def main() -> None:
    filename = input("Enter name of the file: ")
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    with open(filename + ".txt", "w") as file:
        for line in lines:
            file.write(line + "\n")

    print(f"File '{filename}.txt' has been created with your content.")


if __name__ == "__main__":
    main()
