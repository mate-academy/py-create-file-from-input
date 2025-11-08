def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    with open(file_name, "w") as file:
        lines = []
        line_text = input("Enter new line of content: ")
        while line_text != "stop":
            lines.append(line_text)
            line_text = input("Enter new line of content: ")

        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
