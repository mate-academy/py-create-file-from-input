import os


def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    with open(file_name, "a") as f:
        new_line = input("Enter new line of content: ")
        f.write(new_line)
        while new_line != "stop":
            f.write("\n" + new_line)
            new_line = input("Enter new line of content: ")

    if os.path.isfile(file_name) and os.stat(file_name).st_size > 0:
        print(f"File '{file_name}' has been created.")

    else:
        print(f"File '{file_name}' is empty or does not exist.")


if __name__ == "__main__":
    main()
