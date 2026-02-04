def main() -> object:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as f:
        while True:
            file_data = str(input("Enter new line of content: "))
            if file_data == "stop":
                break
            f.write(f"{file_data}\n")
    return f


if __name__ == "__main__":
    main()
