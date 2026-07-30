def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []
    while True:
        line = input("Enter new line of content: ")

        if line == "stop":
            break
        lines.append(line)

    with open(f"{file_name}.txt", "a") as f:
        for i in lines:
            f.write(i + "\n")


if __name__ == "__main__":
    main()
