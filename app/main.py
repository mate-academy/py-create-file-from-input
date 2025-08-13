def main() -> None:
    file_name = input("name of the file: ")
    stop = False

    if file_name[len(file_name) - 4:] != "txt":
        file_name += ".txt"

    while not stop:
        content = input("Enter new line of content: ")
        if content.lower() == "stop":
            stop = True
        else:
            content += "\n"
            with open(f"../{file_name}", "a") as output_file:
                output_file.write(content)
                output_file.close()


if __name__ == "__main__":
    main()
