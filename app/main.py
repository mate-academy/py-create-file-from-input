import os


def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    if os.path.exists(file_name):
        raise FileExistsError(
            f"Error: The file '{file_name}' already exists.")

    with open(file_name, "x") as file:
        while True:
            next_line = input("Enter new line of content: ")
            if next_line == "stop":
                break
            file.write(next_line + "\n")


if __name__ == "__main__":
    main()
