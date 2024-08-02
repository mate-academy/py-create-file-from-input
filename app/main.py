def main() -> None:
    name_of_the_file = input("Enter name of the file: ")
    with open(f"{name_of_the_file}.txt", "w") as editing_file:
        while True:
            content_on_line = input("Enter new line of content: ")

            if content_on_line == "stop":
                break

            editing_file.write(f"{content_on_line}\n")


if __name__ == "__main__":
    main()
