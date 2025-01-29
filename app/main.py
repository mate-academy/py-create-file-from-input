def main() -> None:
    file_name = input("Enter name of the file: ")
    new_line = input("Enter new line of content: ")
    result = []
    while new_line != "stop":
        result.append(f"{new_line}\n")
        new_line = input("Enter new line of content: ")

    with open(f"{file_name}.txt", "w") as f:
        f.writelines(result)


if __name__ == "__main__":
    main()
