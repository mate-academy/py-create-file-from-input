def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    str_memory = ""

    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        str_memory += user_input + "\n"

    with open(file_name, "w") as f:
        f.write(str_memory)


if __name__ == "__main__":
    main()
