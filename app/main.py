def main() -> None:
    file_basename = input("Enter name of the file: ")
    filename = f"{file_basename}.txt"

    open(filename, "w").close()

    while True:
        word_line = input("Enter new line of content: ")

        if word_line == "stop":
            break

        with open(filename, "a") as f:
            f.write(f"{word_line}\n")


if __name__ == "__main__":
    main()
