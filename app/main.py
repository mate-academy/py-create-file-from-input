def main() -> None:
    name = input("Enter name of the file: ")

    lines = []
    while True:
        command = input("Enter new line of content: ")
        if command == "stop":
            break
        lines.append(command)

    with open(f"{name}.txt", "w") as file:
        for line in lines:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
