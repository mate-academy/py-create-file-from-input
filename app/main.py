def main() -> None:
    # write your code here
    file_name = input("Enter name of the file: ")

    content = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)

    file_name = file_name + ".txt"
    with open(file_name, "w") as file:
        for line in content:
            file.write(line + "\n")

    print(f"\nFile name: '{file_name}'\nFile content:\n")
    with open(file_name, "r") as file:
        print(file.read())


if __name__ == "__main__":
    main()
