def main() -> None:
    file_name = input("Enter file name: ")
    file = open(f"{file_name}", "a")
    input_content = ""
    while input_content != "stop":
        input_content = input("Enter content: ")
        file.write(input_content)

if __name__ == "__main__":
    main()
