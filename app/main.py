def main() -> None:

    zero_list = []

    name_file = input("Enter name of the file: ")
    if not name_file.endswith(".txt"):
        name_file += ".txt"

    with open(name_file, "w") as f:

        while True:
            user_line = input("Enter new line of content: ")
            if user_line == "stop":
                break
            zero_list.append(user_line)

        for line in zero_list:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
