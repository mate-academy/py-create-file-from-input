def main() -> object:
    file_name = input("Enter name of the file")
    file_name = file_name + ".txt"
    new_line = ""
    with open(file_name, "a") as f:
        while new_line != "stop":
            new_line = input("Enter new line of content")
            f.write(f"{new_line}\n")
        print(f"new file {file_name} created")


if __name__ == "__main__":
    main()
