def main() -> None:
    name = input("Enter name of the file: ")
    name = name + ".txt"
    new_list = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        new_list.append(line)

    with open(name, "w") as file:
        for line in new_list:
            file.write(
                f"{line}\n"
            )


if __name__ == "__main__":
    main()
