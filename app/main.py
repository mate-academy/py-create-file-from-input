
def main() -> None:
    file_name = input("Enter name of the file: ")
    file_data = ""
    while True:
        data = input("Enter new line of content: ")
        if data == "stop":
            break
        file_data += data + "\n"
    with open(f"{file_name}.txt", "w") as f:
        f.write(file_data)


if __name__ == "__main__":
    main()
