def main() -> None:
    file_name = input("Enter name of the file: ")
    num_line = 1
    with open(f"{file_name}.txt", "a") as file:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            file.write(line + "\n")
            num_line += 1


if __name__ == "__main__":
    main()
