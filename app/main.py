def main():
    name = input("Enter name of the file: ")
    content = ''

    while True:
        line = input("Enter new line of content: ")

        if line == "stop":
            break

        content += f"{line}\n"

    with open(f"{name}.txt", 'w') as f:
        f.write(content)


if __name__ == "__main__":
    main()
