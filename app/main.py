def main() -> None:
    input_line = input("Enter name of the file: ")
    input_data = [input_line]

    while True:
        input_line = input("Enter new line of content: ")
        if input_line == "stop":
            break
        input_data.append(input_line)

    result_file = open(f"{input_data[0]}.txt", "x")

    for line in range(1, len(input_data)):
        result_file.write(f"{input_data[line]}\n")

    result_file.close()


if __name__ == "__main__":
    main()
