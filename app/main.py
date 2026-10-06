def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        file_content.append(f"{line}\n")

    r_file = f"{file_name}.txt"
    final_file = open(r_file, "w")
    final_file.writelines(file_content)
    final_file.close()


if __name__ == "__main__":
    main()
