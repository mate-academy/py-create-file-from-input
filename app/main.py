from typing import Any


def main() -> Any:
    name = input("Enter name of the file: ")
    file_name = name + ".txt"
    file1 = open(file_name, "w")
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        file1.write(new_line + "\n")
    file1.close()


if __name__ == "__main__":
    main()
