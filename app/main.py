from typing import List


def main() -> None:
    file_name: str = input("Enter name of the file: ")
    file_content: List[str] = []

    while True:
        line: str = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        file_content.append(line)

    file_path: str = file_name + ".txt"
    with open(file_path, "w") as file:
        for line in file_content:
            file.write(line + "\n")

    print(f"File name: \"{file_path}\"")
    print("File content:")
    for line in file_content:
        print("#", line)


if __name__ == "__main__":
    main()
