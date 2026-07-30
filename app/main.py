def main() -> None:
    file_name = input("Enter name of the file: ")

    while True:
        line = input("Enter new line of content: ")

        with open(file_name + ".txt", "a") as f:
            if line == "stop":
                break

            f.write(line + "\n")


if __name__ == "__main__":
    main()
