def main() -> None:

    name_of_file = input("Enter name of the file: ") + ".txt"
    input_messages = []

    while True:
        line = input("Enter new line of content: ")

        if line.lower() == "stop":
            break  # Exit the loop when "stop" is entered
        else:
            input_messages.append(line)

    with open(name_of_file, "a") as current_file:
        current_file.write("\n".join(input_messages))


if __name__ == "__main__":
    main()
