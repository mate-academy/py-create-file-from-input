def main() -> None:
    file_name = input("Enter name of the file: ")
    file_write = open(f"{file_name}.txt", "w")
    print(f"File name: '{file_name}.txt'")
    file_string = ""
    print("File content:")
    while file_string != "stop":
        file_string = ""
        file_string = input("Enter new line of content: ")
        if file_string != "stop":
            file_write.write(file_string + "\n")
            print(f"{file_string}\n")
    file_write.close()


if __name__ == "__main__":
    main()
