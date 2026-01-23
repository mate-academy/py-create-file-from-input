def main() -> None:
    file_name = input("Enter name of the file: ")
    text = ""
    while True:
        new_line = input("Enter new line of content: ")
        if new_line.lower() == "stop":
            break
        text += f"{new_line}\n"
    output_file = open(file_name + ".txt", "w")
    output_file.write(text)
    output_file.close()


if __name__ == "__main__":
    main()
