def main() -> None:
    enter_the_file_name = input("Enter name of the file: ")
    with open(f"{enter_the_file_name}.txt", "a") as users_file:
        while True:
            enter_the_file_line = input("Enter new line of content: ")
            if enter_the_file_line.strip().lower() == "stop":
                break
            users_file.write(f"{enter_the_file_line.strip()}\n")


if __name__ == "__main__":
    main()
