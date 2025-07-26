def main():
    file_name = input("Enter the name of the file: ")
    full_file_name = file_name + ".txt"


    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(full_file_name, "w") as file:
        for line in lines:
            file.write(line + "\n")

    print(f'✅ File "{full_file_name}" created successfully with {len(lines)} lines.')


if __name__ == "__main__":
    main()
