def main() -> None:
    file_name = input("Enter name of the file: ")

    lines = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            with open(f"{file_name}.txt", "w") as file:
                file.write("\n".join(lines))
            break

        lines.append(new_line)


if __name__ == "__main__":
    main()
