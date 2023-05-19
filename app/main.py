def main() -> None:
    file_name: str = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "w") as file:
        while True:
            content: str = input("Enter new line of content: ")
            if content.lower() == "stop":
                break
            file.write(f"{content}\n")


if __name__ == "__main__":
    main()
