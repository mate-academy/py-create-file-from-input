def main() -> None:
    name_of_file = input("Enter name of the file: ")
    with open(f"{name_of_file}.txt", "w") as f:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            f.write(content + "\n")


if __name__ == "__main__":
    main()
