def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = file_name + ".txt"
    with open(file_name, "w") as f:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            f.write(line + "\n")


if __name__ == "__main__":
    main()
