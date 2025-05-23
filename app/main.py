def main() -> None:
    file_name = input("Enter name of the file: ")
    if file_name:
        with open(f"{file_name}.txt", "w") as file:
            while True:
                content = input("Enter new line of content: ")
                if content == "stop":
                    break
                file.write(f"{content}\n")
    pass


if __name__ == "__main__":
    main()
