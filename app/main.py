def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as user_file:
        count = 1
        while True:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            if count != 1:
                user_file.write(f"\n{new_line}")
            else:
                user_file.write(new_line)
            count += 1


if __name__ == "__main__":
    main()
