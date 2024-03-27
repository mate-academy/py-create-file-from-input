
def main() -> None:
    file_name = input("Enter name of the file: ")
    content = str()
    while True:
        line_of_content = input("Enter new line of content: ")
        if line_of_content == "stop":
            break
        content += f"{line_of_content}\n"
    with open(f"{file_name}.txt", "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
