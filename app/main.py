def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w", encoding="utf-8") as f:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            print(line, file=f)


if __name__ == "__main__":
    main()
