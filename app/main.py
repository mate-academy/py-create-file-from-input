def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = []
    while True:
        answer = input("Enter new line of content: ")

        if answer.lower() == "stop":
            break

        content.append(answer)

    with open(file_name, "w") as f:
        for line in content:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
