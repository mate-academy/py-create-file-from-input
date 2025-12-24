import os
from typing import List


def main() -> None:
    file_name: str = input("Enter name of the file: ")

    if os.path.isfile(f"{file_name}.txt"):
        response: str = input(f"File '{file_name}.txt' already exists. "
                              f"Do you want to overwrite it? (yes/no): ")
        if response.lower() != "yes":
            print("File was not created.")
            return

    file_content: List[str] = []

    while True:
        line: str = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        file_content.append(line)

    try:
        with open(f"{file_name}.txt", "w") as file:
            file.write("\n".join(file_content))
        print(f"File '{file_name}.txt' was successfully created "
              f"and filled with content.")
    except IOError:
        print("Error while working with the file. "
              "Please check the file name or try again.")


if __name__ == "__main__":
    main()
