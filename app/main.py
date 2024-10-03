def main() -> None:
    file_name = input("Enter name of the file: ")

    file_name = f"{file_name}.txt"

    with open(file_name, "w"):
        pass

    while True:
        file_content = input("Enter new line of content: ")
        if file_content == "stop":
            break

        with open(f"{file_name}", "a") as f:
            f.write(f"{file_content}\n")


if __name__ == "__main__":
    main()
