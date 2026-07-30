def main() -> None:
    input_name_file = input("Enter name of the file: ")

    with open(input_name_file + ".txt", "w") as f:

        while True:
            input_content = input("Enter new line of content: ")
            if input_content.lower() == "stop":
                break
            f.write(input_content + "\n")


if __name__ == "__main__":
    main()
