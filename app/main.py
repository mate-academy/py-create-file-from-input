from typing import List, Text


def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content: List[Text] = []

    while True:
        new_line = input("Enter new line of content: ")
        if new_line.lower() == "stop":
            break
        file_content.append(new_line)

    full_file_name = f"{file_name}.txt"

    try:
        with open(full_file_name, "w") as file:
            for line in file_content:
                file.write(line + "\n")
        print(f"File '{full_file_name}' created successfully.")

    except OSError as error:
        print(f"Error creating file: {error}")


if __name__ == "__main__":
    main()
