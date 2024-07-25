def main() -> None:
    file_name = input("Enter name of the file: ")
    result = ""
    line = ""
    while line != "stop":
        if not line:
            result += line
        else:
            result += line + "\n"
        line = input("Enter new line of content: ")
    with open(file_name + ".txt", "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()
