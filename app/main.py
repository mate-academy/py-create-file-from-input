def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "w") as f:
        while True:
            next_line = input("Enter new line of content: ")

            if next_line.lower() == "stop":
                break
            f.write(next_line + "\n")


if __name__ == "__main__":
    main()
