def main():
    content = []
    file_name = input("Enter name of the file: ")

    if file_name:
        while True:
            value = input("Enter new line of content: ")
            if value == "stop":
                break
            content.append(value)

    created_file = open(f"{file_name}.txt", "a")

    created_file.write("\n".join(content))

    created_file.close()


if __name__ == "__main__":
    main()
