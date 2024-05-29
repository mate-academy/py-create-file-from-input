def main():
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as file_add_info:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            file_add_info.write(content + "\n")


if __name__ == "__main__":
    main()
