def main() -> None:
    file_name = input("Enter name of the file: ")

    output_file = open(f"{file_name}.txt", "w")

    while True:
        entered_text = input("Enter new line of content: ")

        if entered_text == "stop":
            break

        output_file.write(entered_text + "\n")

    output_file.close()


if __name__ == "__main__":
    main()
