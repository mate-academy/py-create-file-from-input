def main() -> None:
    file_name = input("Enter name of the file: ")
    is_stopped = False
    lines = []

    while is_stopped is False:
        line_of_code = input("Enter new line of content: ")

        if line_of_code == "stop":
            break

        if line_of_code:
            lines.append(line_of_code)

    with open(f"{file_name}.txt", "a") as file:
        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
