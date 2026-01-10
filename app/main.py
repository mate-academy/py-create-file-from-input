def main() -> None:
    file_name = input("Enter name of the file: ")
    new_file_name = f"{file_name}.txt"

    with open(new_file_name, "w") as f:

        while True:
            user_input = input("Enter new line of content: ")
            if user_input.lower() == "stop":
                break

            f.write(f"{user_input}\n")


if __name__ == "__main__":
    main()
