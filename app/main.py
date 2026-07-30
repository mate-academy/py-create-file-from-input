def main() -> None:
    name_input = input("Enter name of the file: ")
    result_file = open(f"{name_input}.txt", "w")
    while True:
        value_input = input("Enter new line of content: ")
        if value_input == "stop":
            break
        result_file.write(f"{value_input}\n")


if __name__ == "__main__":
    main()
