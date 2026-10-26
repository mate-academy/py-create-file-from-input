def main() -> None:
    filename = input("Enter name of the file: ")

    line_list = []
    line_1 = input("Enter new line of content: ")
    while line_1 != "stop":
        line_list.append(line_1)
        line_1 = input("Enter new line of content: ")

    with open(f"{filename}.txt", "w") as file:
        file.write("\n".join(line_list))


if __name__ == "__main__":
    main()
