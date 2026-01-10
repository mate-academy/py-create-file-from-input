def main() -> None:
    file_name = input("Enter name of the file: ")
    result = ""
    while True:
        word = input("Enter new line of content: ")
        if word == "stop":
            break
        result += f"{word}\n"

    with open(f"{file_name}.txt", "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()
