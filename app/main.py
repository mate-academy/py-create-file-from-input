from typing import Any


def main() -> Any:
    file_name = input("Enter name of the file: ") + ".txt"
    file_data = ""

    while True:
        line_input = input("Enter new line of content: ")
        if line_input == "stop":
            break
        file_data += f"{line_input}\n"

    with open(file_name, "w") as f:
        f.write(file_data)


if __name__ == "__main__":
    main()
