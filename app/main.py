def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as f:
        pass
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        with open(f"{file_name}.txt", "a") as f:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
