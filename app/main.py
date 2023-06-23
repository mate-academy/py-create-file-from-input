def main():
    file_name = input("Enter name of the file: ")
    file_content = []
    while True:
        content = input("Enter new line of content or 'stop' to exit: ")
        if content == "stop":
            break

    with open(file_name, "w") as f:
        for content in file_content:
            f.write(content)

if __name__ == "__main__":
    main()
