def main() -> None:
    file_list = []
    fn = input("Enter name of the file: ")
    file_name = f"{fn}.txt"
    while True:
        file_content = input("Enter new line of content: ")
        if file_content == "stop":
            break
        file_list.append(file_content)
    with open(file_name, "w") as file:
        for item in file_list:
            file.write(f"{item}\n")


if __name__ == "__main__":
    main()
