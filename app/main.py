def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "w", encoding="utf-8") as file:
        file.write(f'File name: "{name}.txt"\n')
        file.write("File content: " + "\n")
        while True:
            file_content = input("Enter file content: ")
            if file_content == "stop":
                break
            else:
                file.write(f"{file_content}\n")
    print("end")


if __name__ == "__main__":
    main()
