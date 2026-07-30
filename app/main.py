def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "a") as opened_file_a_mode:
        while True:
            content_string = input("Enter new line of content: ")
            if content_string == "stop":
                break
            opened_file_a_mode.write(content_string + "\n")


if __name__ == "__main__":
    main()
