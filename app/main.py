def main() -> None:
    file_name = input("Enter name of the file: ")
    result = ""
    while True:
        next_line = input("Enter new line of content: ")
        if next_line == "stop":
            break
        result += f"{next_line}\n"
    with open(f"{file_name}.txt", "a") as f:
        f.write(result)


if __name__ == "__main__":
    main()
