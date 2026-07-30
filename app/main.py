def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"

    with open(file_name, "w") as f:
        while True:
            content = input("Enter new line of content: ")

            if content == "stop":
                break

            f.write(content)
            f.write("\n")


if __name__ == "__main__":
    main()
