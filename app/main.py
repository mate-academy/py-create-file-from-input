def main():
    file_name = input("Enter name of the file: ")

    with open(file_name, "a") as file:
        file.write(f'File name: "{file_name}.txt"\nFile content:\n')
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            file.write(f"{content}\n")


if __name__ == "__main__":
    main()
