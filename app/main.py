def main() -> None:
    file_name = input("Enter name of the file: ")
    if file_name:
        with open(f"{file_name}.txt", "a") as file:
            while True:
                new_line = input("Enter new line of content: ")
                if new_line == "stop":
                    break
                file.write(new_line + "\n")


if __name__ == "__main__":
    main()
