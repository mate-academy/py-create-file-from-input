def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "a") as f:
        while True:
            line_of_content = input("Enter new line of content: ")
            if line_of_content == "stop":
                break
            f.write(line_of_content + "\n")


if __name__ == "__main__":
    main()
