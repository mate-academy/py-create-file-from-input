def main() -> None:
    name = input("Enter name of the file: ")

    line_list = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        line_list.append(line)

    with open(f"{name}.txt", "w") as file:
        for i in line_list:
            file.write(i + "\n")


if __name__ == "__main__":
    main()
