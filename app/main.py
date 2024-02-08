def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []
    while True:
        input_line = input("Enter new line of content: ")

        if input_line != "stop":
            content.append(input_line)
        else:
            break
    with open(f"{file_name}.txt", "w") as f:
        for line in content:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
