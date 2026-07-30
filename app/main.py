def main() -> None:
    file_basename = input("Enter name of the file: ")
    with open(f"{file_basename}.txt", "w") as f:
        newline = ""
        while newline != "stop\n":
            f.write(newline)
            newline = input("Enter new line of content: ")
            newline += "\n"


if __name__ == "__main__":
    main()
