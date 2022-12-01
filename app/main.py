def main() -> None:
    file_name = input("Enter name of the file: ")
    text = input("Enter new line of content: ")
    with open(file_name, "w") as file:
        while True:
            text = input("Enter new line of content: ")
            file.write(text + "\n")
            if text == "stop":
                break
    with open(f"{file_name}.txt", "r") as f:
        print(f"File name: {file_name}.txt\nFile content:")
        print(f.read())


if __name__ == "__main__":
    main()
