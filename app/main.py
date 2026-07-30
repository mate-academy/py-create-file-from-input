def main() -> None:
    name = input("Enter name of the file: ")
    if not name.endswith(".txt"):
        name += ".txt"
    result_list = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        result_list.append(new_line)
    with open(name, "w") as out:
        for line in result_list:
            out.write(line + "\n")


if __name__ == "__main__":
    main()
