def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    print(file_name)
    with open(file_name, "a") as f:
        while 1:
            next_line = input("Enter new line of content: ")
            if next_line == "stop":
                break
            f.write(next_line + "\n")


if __name__ == "__main__":
    main()
