def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as f:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line != "stop":
                f.write(f"{new_line}\n")
            else:
                break


if __name__ == "__main__":
    main()
