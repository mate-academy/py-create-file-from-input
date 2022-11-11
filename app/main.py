def main():
    file_name = input("Enter name of the file: ")
    content = input("Enter new line of content: ")

    with open(f"{file_name}.txt", "w") as f:

        while content != "stop":
            print(f.write(f"{content}\n"))
            content = input("Enter new line of content: ")
            if content == "stop":
                break

    with open(f"{file_name}.txt", "r") as f:
        print(f"File name: {file_name}.txt\nFile content:")
        print(f.read())


if __name__ == "__main__":
    main()
