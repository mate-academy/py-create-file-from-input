def main() -> None:
    file_name = input("Enter name of the file: ")

    while True:
        new_line = input("Enter new line of content: ")
        with open(f"{file_name}.txt", "a") as f:
            if new_line == "stop":
                break
            f.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
