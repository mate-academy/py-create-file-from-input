def enter_name() -> str:
    while True:
        input_str = input("Enter name of the file: ").strip().lower()
        if input_str == "stop":
            continue
        if input_str:
            break
    if not input_str.endswith(".txt"):
        input_str += ".txt"
    return input_str


def main() -> None:
    file_name = enter_name()

    with open(file_name, "w") as file:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line.strip() == "stop":
                break
            file.write(new_line + "\n")


if __name__ == "__main__":
    main()
