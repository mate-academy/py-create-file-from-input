def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    all_txt_in_file = []
    while True:
        file_interion = input("Enter new line of content: ")
        all_txt_in_file.append(file_interion)
        if file_interion == "stop":
            break
    all_txt_in_file.pop(-1)
    with open(file_name, "w") as file:
        for line in all_txt_in_file:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
