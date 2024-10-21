def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = ""
    with open(f"{file_name}.txt", "a") as file:

        while True:
            file_content = input("Enter new line of content: ")
            if file_content == "stop":
                break
            file.write(f"{file_content}\n")


if __name__ == "__main__":
    main()
