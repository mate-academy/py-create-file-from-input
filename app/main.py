def main() -> None:

    file_name = input("Enter name of the file: ")

    lines = []

    with open(file_name + ".txt", "a") as file:

        while True:

            line = input("Enter new line of content: ")
            if line == "stop":
                break
            lines.append(line)

        file.writelines("\n".join(lines))


if __name__ == "__main__":
    main()
