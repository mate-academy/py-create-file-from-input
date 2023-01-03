def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as file:
        while True:
            info = input("Enter new line of content: ")
            if info == "stop":
                break
            file.write(f"{info}\n")


if __name__ == "__main__":
    main()
