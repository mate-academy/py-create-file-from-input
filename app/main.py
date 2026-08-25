import os


def main() -> None:
    file_name = input("Enter name of the file: ")
    path_file = os.path.join(os.getcwd(), f"{file_name}.txt")
    new_file = open(path_file, "a")

    input_text = ""
    while input_text != "stop":
        input_text = input("Enter new line of content: ")
        if input_text == "stop":
            break
        new_file.write(f"{input_text}\n")

    new_file.close()


if __name__ == "__main__":
    main()
