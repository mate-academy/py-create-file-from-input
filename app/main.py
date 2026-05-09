def main() -> None:
    lines = []
    data_of_user = input("Enter name of the file: ")
    new_line = input("Enter new line of content: ")
    while new_line != "stop":
        lines.append(new_line + "\n")
        new_line = input("Enter new line of content: ")

    with open(f"{data_of_user}.txt", "w") as file:
        file.write("".join(lines))


if __name__ == "__main__":
    main()
