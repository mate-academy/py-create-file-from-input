def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "a") as f:
        while True:
            line = input("Enter new line of content: ")
            if line.lower() == "stop":
                break
            f.write(line + "\n")


if __name__ == "__main__":
    main()
