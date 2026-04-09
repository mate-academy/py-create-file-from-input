def main() -> None:
    file_name = input("Enter name of the file: ")
    if len(file_name) > 0:
        file_name = file_name.strip() + ".txt"
        file_output = open(file_name, "w")
        file_output.write(f"File name: {file_name}\n")
        file_output.write("File content:\n")
        while True:
            input_line = input("Enter new line of content: ")
            if "stop" in input_line:
                break
            file_output.write(f"{input_line}\n")
        file_output.close()


if __name__ == "__main__":
    main()
