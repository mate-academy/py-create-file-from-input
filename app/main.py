def main() -> None:
    file_name = input("Enter name of the file: ")
    contex = []
    while True:
        line = input("Enter new line of content: ")

        if line == "stop":
            break

        contex.append(line)

    with open(f"{file_name}.txt", "w") as file:
        for line in contex:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
