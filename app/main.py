def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    with open("new_file.txt", "a") as file:
        file.write(f"File name: {file_name}")
        file.write("File content:")
        while True:
            baka = input("Enter new line of content: ")
            if baka.lower() == "stop":
                break
            file.write(f"{baka}" + "\n")


if __name__ == "__main__":
    main()
