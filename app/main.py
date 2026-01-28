def main() -> None:

    file_name = input("Enter name of the file: ")

    output_file = open(f"{file_name}.txt", "w")

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        output_file.write(f"{line}\n")

    output_file.close()


if __name__ == "__main__":
    main()
