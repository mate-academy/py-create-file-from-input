def main() -> None:
    file_name = input("Enter name of the file: ")
    open(f"{file_name}.txt", "w")
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        else:
            with open(f"{file_name}.txt", "a") as file:
                file.write(f"{line}\n")


if __name__ == "__main__":
    main()
