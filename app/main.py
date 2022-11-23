def main() -> None:
    file_name = input("Enter name of the file: ")
    if file_name:
        with open(f"{file_name}" + ".txt", "a") as file:
            while True:
                input_content = input("Enter new line of content: ")
                if input_content == "stop":
                    break
                file.write(input_content + "\n")


if __name__ == "__main__":
    main()
