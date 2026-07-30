def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line + "\n")

    full_file_name = file_name + ".txt"
    try:
        with open(full_file_name, "w") as file:
            file.writelines(content)
        print(f"File {full_file_name} sucsesfull created.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")


if __name__ == "__main__":
    main()
